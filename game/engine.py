"""
Core game engine — deck management and state transitions.
All functions take and return plain dicts (stored in Flask session).
"""
import random
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
    return card_id, state


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
    """Shuffle a specific card back into the draw deck."""
    # Remove from log or discard if it ended up there
    for pile in ("log_pile", "discard_pile"):
        if card_id in state[pile]:
            state[pile].remove(card_id)
    if card_id not in state["draw_deck"]:
        state["draw_deck"].append(card_id)
        random.shuffle(state["draw_deck"])
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

def update_resource(state: dict, resource: str, delta: int) -> dict:
    if resource in state["resources"]:
        state["resources"][resource] = max(0, state["resources"][resource] + delta)
    return state


# ── Turn helpers ──────────────────────────────────────────────────────────────

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

    return {
        "card":          card,
        "active_traits": active_traits,
        "action_entry":  action_entry,
        "has_do":        state["has_duty_officer"],
    }


# ── Deck stats helper ─────────────────────────────────────────────────────────

def deck_stats(state: dict) -> dict:
    return {
        "draw":    len(state["draw_deck"]),
        "discard": len(state["discard_pile"]),
        "reserve": len(state["reserve_deck"]),
        "log":     len(state["log_pile"]),
    }
