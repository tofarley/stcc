"""
Core game engine — deck management and state transitions.
All functions take and return plain dicts (stored in Flask session).
"""
import random
import re
from typing import Optional

from game.data import (
    common,
    shran   as shran_data,
    picard  as picard_data,
    koloth  as koloth_data,
    sisko   as sisko_data,
    sela    as sela_data,
    burnham as burnham_data,
)

CAPTAINS = {
    "shran":   shran_data,
    "picard":  picard_data,
    "koloth":  koloth_data,
    "sisko":   sisko_data,
    "sela":    sela_data,
    "burnham": burnham_data,
}


# ── Card lookup ───────────────────────────────────────────────────────────────

def get_card(card_id: str) -> Optional[dict]:
    """Return card dict for any card ID (captain deck or common pool)."""
    # Try captain-specific decks first
    for module in CAPTAINS.values():
        if card_id in module.BY_ID:
            return module.BY_ID[card_id]
    # Fall back to common pool
    return common.BY_ID.get(card_id)


def get_captain_module(captain_id: str):
    return CAPTAINS[captain_id]


# ── Game initialisation ───────────────────────────────────────────────────────

def initialize_game(captain_id: str) -> dict:
    module = get_captain_module(captain_id)
    cards = module.CARDS

    available     = [c["id"] for c in cards if c["starting_location"] == "available"]
    deployed      = [c["id"] for c in cards if c["starting_location"] == "deployed"]
    controlled    = [c["id"] for c in cards if c["starting_location"] == "controlled_location"]
    development   = [c["id"] for c in cards if c["starting_location"] == "development"]
    reserve       = [c["id"] for c in cards if c["starting_location"] == "reserve"]
    discard_start = [c["id"] for c in cards if c["starting_location"] == "discard"]
    captain_card  = next((c["id"] for c in cards if c["starting_location"] == "captain"), None)
    # status cards (Burnham) are set aside face-up, not in any deck
    status_cards  = [c["id"] for c in cards if c["starting_location"] == "status"]
    # incident_deck cards go to the shared incident pile, not the bot's decks
    # (tracked for display but not put in draw/reserve)

    # Draw deck: shuffle available, then place (deployed + controlled) on top
    random.shuffle(available)
    top_cards = deployed + controlled
    random.shuffle(top_cards)
    draw_deck = top_cards + available

    # Reserve deck: reserve cards on top, development cards shuffled beneath
    random.shuffle(reserve)
    random.shuffle(development)
    reserve_deck = reserve + development

    return {
        "captain_id":       captain_id,
        "draw_deck":        draw_deck,
        "discard_pile":     discard_start,
        "reserve_deck":     reserve_deck,
        "log_pile":         [],
        "captain_card":     captain_card,
        "status_cards":     status_cards,
        "has_duty_officer": False,
        "duty_officer_card": None,
        "resources": {
            "latinum":   0,
            "glory":     0,
            "dilithium": 0,
            "research":  0,
            "influence": 0,
            "military":  0,
        },
        "current_turn_cards": [],
        "deployed_cards":     [],
        "warped_ships":       {},
    }


# ── Deck refresh ──────────────────────────────────────────────────────────────

def _refresh_deck(state: dict) -> dict:
    """
    Shuffle discard pile into a new draw deck, then place the top reserve
    card on top.  Called automatically when the draw deck is empty.
    """
    new_draw = state["discard_pile"][:]
    random.shuffle(new_draw)
    state["discard_pile"] = []

    if state["reserve_deck"]:
        top_reserve = state["reserve_deck"].pop(0)
        new_draw.insert(0, top_reserve)

    state["draw_deck"] = new_draw
    return state


def _ensure_draw_deck(state: dict) -> dict:
    if not state["draw_deck"] and state["discard_pile"]:
        state = _refresh_deck(state)
    return state


# ── Draw / discard / log operations ──────────────────────────────────────────

def draw_card(state: dict) -> tuple[Optional[str], dict]:
    """Pop the top card from the draw deck. Returns (card_id | None, state)."""
    state = _ensure_draw_deck(state)
    if not state["draw_deck"]:
        return None, state
    card_id = state["draw_deck"].pop(0)
    state.setdefault("current_turn_cards", []).append(card_id)
    return card_id, state


def discard_drawn_cards(state: dict) -> tuple[list[str], dict]:
    """
    Move all drawn-but-unresolved cards to the discard pile (end of turn cleanup).
    Cards already in log, deployed, warped, or serving as Duty Officer are skipped.
    Clears current_turn_cards.  Returns (list of discarded card_ids, state).
    """
    already_resolved = set(state.get("log_pile", []))
    already_resolved.update(state.get("deployed_cards", []))
    already_resolved.update(state.get("warped_ships", {}).keys())
    if state.get("duty_officer_card"):
        already_resolved.add(state["duty_officer_card"])

    discarded = []
    for card_id in state.get("current_turn_cards", []):
        if card_id not in already_resolved and card_id not in state["discard_pile"]:
            state["discard_pile"].append(card_id)
            discarded.append(card_id)

    state["current_turn_cards"] = []
    return discarded, state


def discard_top(state: dict, count: int) -> tuple[list[str], dict]:
    """
    Move the top `count` cards from the draw deck to the discard pile.
    Returns (list of discarded card_ids, updated state).
    Handles mid-discard deck refresh automatically.
    """
    discarded = []
    for _ in range(count):
        state = _ensure_draw_deck(state)
        if not state["draw_deck"]:
            break
        card_id = state["draw_deck"].pop(0)
        state["discard_pile"].append(card_id)
        discarded.append(card_id)
    return discarded, state


def log_top_card(state: dict) -> tuple[Optional[str], dict]:
    """Log (permanently remove) the top card of the draw deck."""
    state = _ensure_draw_deck(state)
    if not state["draw_deck"]:
        return None, state
    card_id = state["draw_deck"].pop(0)
    state["log_pile"].append(card_id)
    return card_id, state


def log_card(state: dict, card_id: str) -> dict:
    """Log a specific card — remove it from wherever it currently is."""
    for pile in ("draw_deck", "discard_pile"):
        if card_id in state[pile]:
            state[pile].remove(card_id)
            break
    if card_id not in state["log_pile"]:
        state["log_pile"].append(card_id)
    return state


def return_card_to_deck(state: dict, card_id: str) -> dict:
    """Return a specific card to the bottom of the draw deck."""
    # Remove from log or discard if it ended up there
    for pile in ("log_pile", "discard_pile"):
        if card_id in state[pile]:
            state[pile].remove(card_id)
    if card_id not in state["draw_deck"]:
        state["draw_deck"].append(card_id)
    return state


def gain_card(state: dict, card_id: str) -> dict:
    """Add a card (common pool or otherwise) to the bot's discard pile."""
    state["discard_pile"].append(card_id)
    return state


# ── Duty officer ──────────────────────────────────────────────────────────────

def promote_duty_officer(state: dict, card_id: str) -> dict:
    """Promote a card to duty officer status."""
    state["has_duty_officer"] = True
    state["duty_officer_card"] = card_id
    return state


def log_duty_officer(state: dict) -> dict:
    """Log the current duty officer (removes from game, clears DO status)."""
    if state["duty_officer_card"]:
        state = log_card(state, state["duty_officer_card"])
    state["has_duty_officer"] = False
    state["duty_officer_card"] = None
    return state


def dismiss_duty_officer(state: dict) -> dict:
    """Dismiss duty officer — card goes to discard (not logged)."""
    if state["duty_officer_card"]:
        card_id = state["duty_officer_card"]
        # Only discard if not already elsewhere
        if card_id not in state["discard_pile"] and card_id not in state["draw_deck"]:
            state["discard_pile"].append(card_id)
    state["has_duty_officer"] = False
    state["duty_officer_card"] = None
    return state


# ── Resources ─────────────────────────────────────────────────────────────────

_SPECIALTY_TRACKS = {"research", "influence", "military"}


def update_resource(state: dict, resource: str, delta: int) -> dict:
    if resource in state["resources"]:
        val = state["resources"][resource] + delta
        val = max(0, val)
        if resource in _SPECIALTY_TRACKS:
            val = min(15, val)
        state["resources"][resource] = val
    return state


def get_specialty_info(state: dict) -> dict:
    """
    Returns a dict keyed by track name with:
      value       — current track value
      multiplier  — active multiplier at that value
      next_at     — track value needed for next multiplier step (None if maxed)
    """
    module = get_captain_module(state["captain_id"])
    thresholds = getattr(module, "SPECIALTY_THRESHOLDS", {})
    res = state["resources"]
    result = {}
    for track in ("research", "influence", "military"):
        val = res.get(track, 0)
        steps = thresholds.get(track, [])
        current_mult = 1
        next_at = None
        for step in steps:
            if val >= step["at"]:
                current_mult = step["multiplier"]
            else:
                next_at = step["at"]
                break
        result[track] = {"value": val, "multiplier": current_mult, "next_at": next_at}
    return result


# ── Deploy / warp / recall ────────────────────────────────────────────────────

def _remove_from_piles(state: dict, card_id: str) -> dict:
    """Remove a card from draw deck, discard, and log pile (wherever it sits)."""
    for pile in ("draw_deck", "discard_pile", "log_pile"):
        if card_id in state[pile]:
            state[pile].remove(card_id)
    return state


def _remove_from_all(state: dict, card_id: str) -> dict:
    """Remove a card from every tracked location."""
    state = _remove_from_piles(state, card_id)
    state = _ensure_deploy_keys(state)
    if card_id in state["deployed_cards"]:
        state["deployed_cards"].remove(card_id)
    if card_id in state["warped_ships"]:
        del state["warped_ships"][card_id]
    return state


def send_card_to_top(state: dict, card_id: str) -> dict:
    """Remove a card from wherever it is and place it on top of the draw deck."""
    state = _remove_from_all(state, card_id)
    state["draw_deck"].insert(0, card_id)
    return state


def send_card_to_discard(state: dict, card_id: str) -> dict:
    """Remove a card from wherever it is and place it in the discard pile."""
    state = _remove_from_all(state, card_id)
    state["discard_pile"].append(card_id)
    return state


def _ensure_deploy_keys(state: dict) -> dict:
    """Back-fill missing deploy/warp keys for sessions created before this feature."""
    state.setdefault("deployed_cards", [])
    state.setdefault("warped_ships", {})
    return state


def deploy_card(state: dict, card_id: str) -> dict:
    """Move a card to the deployed zone (out of all deck piles)."""
    state = _ensure_deploy_keys(state)
    state = _remove_from_piles(state, card_id)
    if card_id in state["warped_ships"]:
        del state["warped_ships"][card_id]
    if card_id not in state["deployed_cards"]:
        state["deployed_cards"].append(card_id)
    return state


def warp_ship(state: dict, card_id: str, location: str) -> dict:
    """Warp a ship to 'neutral' or 'controlled' planet (out of all deck piles)."""
    state = _ensure_deploy_keys(state)
    state = _remove_from_piles(state, card_id)
    if card_id in state["deployed_cards"]:
        state["deployed_cards"].remove(card_id)
    state["warped_ships"][card_id] = location
    return state


def recall_card(state: dict, card_id: str) -> dict:
    """Return a deployed or warped card to the discard pile."""
    state = _ensure_deploy_keys(state)
    if card_id in state["deployed_cards"]:
        state["deployed_cards"].remove(card_id)
    if card_id in state["warped_ships"]:
        del state["warped_ships"][card_id]
    if card_id not in state["discard_pile"]:
        state["discard_pile"].append(card_id)
    return state


def get_deployed_display(state: dict) -> dict:
    """Return pre-looked-up card data for the deployed/warped panel."""
    state = _ensure_deploy_keys(state)
    deployed = [get_card(cid) for cid in state["deployed_cards"]]
    warped   = [(get_card(cid), loc) for cid, loc in state["warped_ships"].items()]
    return {"deployed": deployed, "warped": warped}


# ── Turn helpers ──────────────────────────────────────────────────────────────

def _detect_gains(text: str) -> tuple[list[str], list[str], list[str]]:
    """
    Scan action text and return (gain_resources, gain_types, take_types).
    - gain_resources: resources to gain or take (effect is the same — increment counter)
    - gain_types: card types instructed with 'gain' (card → bot discard pile)
    - take_types: card types instructed with 'take' (card → top of bot draw deck)
    Uses proximity matching (~50 chars) to avoid false positives like
    'for each Person card in Discard pile'.
    """
    lower = text.lower()
    resources = [
        r for r in ("glory", "latinum", "dilithium")
        if re.search(r'\b(?:gain|take)\b.{0,50}?\b' + r + r'\b', lower, re.DOTALL)
    ]
    gain_types = []
    take_types = []
    for type_name in common.BY_TYPE.keys():
        tl = type_name.lower()
        if re.search(r'\bgain\b.{0,50}?\b' + tl + r'\b', lower, re.DOTALL):
            gain_types.append(type_name)
        if re.search(r'\btake\b.{0,50}?\b' + tl + r'\b', lower, re.DOTALL):
            take_types.append(type_name)
    return resources, gain_types, take_types


def take_card(state: dict, card_id: str) -> dict:
    """Place a card from the common pool directly on top of the bot's draw deck."""
    state["draw_deck"].insert(0, card_id)
    return state


def resolve_card_display(state: dict, card_id: str) -> dict:
    """
    Build the display context for a single drawn card.
    Returns a dict suitable for passing to the card_result template.
    """
    module = get_captain_module(state["captain_id"])
    card = get_card(card_id)

    # Determine active traits on this card
    active_traits = [
        module.TRAITS[t]
        for t in (card.get("traits") or [])
        if t in module.TRAITS
    ]

    # Determine action from duty officer menu
    menu = module.WITH_DUTY_OFFICER if state["has_duty_officer"] else module.NO_DUTY_OFFICER
    action_entry = menu.get(card.get("card_type"), None)

    # Scan all visible action text for gain/take keywords
    texts = [action_entry["action"] if action_entry else ""]
    texts += [t.get("action", "") for t in active_traits]
    gain_resources, gain_types, take_types = _detect_gains(" ".join(texts))

    return {
        "card":           card,
        "active_traits":  active_traits,
        "action_entry":   action_entry,
        "has_do":         state["has_duty_officer"],
        "gain_resources": gain_resources,
        "gain_types":     gain_types,
        "take_types":     take_types,
    }


# ── Deck stats helper ─────────────────────────────────────────────────────────

def deck_stats(state: dict) -> dict:
    return {
        "draw":    len(state["draw_deck"]),
        "discard": len(state["discard_pile"]),
        "reserve": len(state["reserve_deck"]),
        "log":     len(state["log_pile"]),
    }
