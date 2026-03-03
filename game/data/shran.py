# ─────────────────────────────────────────────────────────────────────────────
# SHRAN  (difficulty 2 of 10, CORE set)
# Card names are placeholders — fill in actual names once confirmed.
# Each card has:
#   id               — unique string
#   name             — display name (placeholder bracketed)
#   card_type        — primary symbol / category
#   traits           — extra trait symbols that appear on this card
#   starting_location — captain | available | deployed | controlled_location
#                       reserve | development | discard | incident
# ─────────────────────────────────────────────────────────────────────────────

CAPTAIN_INFO = {
    "id": "shran",
    "name": "Shran",
    "difficulty": "2 of 10",
    "set": "CORE",
}

# Each entry is a list of {"at": N, "multiplier": M} steps in ascending order.
# The active multiplier is the highest step whose "at" value ≤ current track value.
SPECIALTY_THRESHOLDS = {
    "research": [
        {"at": 0,  "multiplier": 1},
        {"at": 5,  "multiplier": 3},
        {"at": 10, "multiplier": 4},
        {"at": 14, "multiplier": 5},
    ],
    "influence": [
        {"at": 0,  "multiplier": 1},
        {"at": 2,  "multiplier": 2},
        {"at": 7,  "multiplier": 3},
        {"at": 10, "multiplier": 4},
        {"at": 13, "multiplier": 5},
        {"at": 15, "multiplier": 6},
    ],
    "military": [
        {"at": 0,  "multiplier": 1},
        {"at": 3,  "multiplier": 2},
        {"at": 8, "multiplier": 3},
        {"at": 11, "multiplier": 5},
        {"at": 15, "multiplier": 6},
    ],
}

# ── Traits ────────────────────────────────────────────────────────────────────
# Resolved first whenever a drawn card carries that trait symbol.
TRAITS = {
    "SURPRISE": {
        "label": "Surprise",
        "action": "Resolve this card's Surprise operation.",
    },
    "WEAPON": {
        "label": "Weapon",
        "action": (
            "Junk the most valuable card in the Market (ignoring any with tokens). "
            "Send a crew member to a neutral Location. "
            "Either you take an Incident OR you remove one token."
        ),
    },
    "ATTACK": {
        "label": "Attack",
        "action": (
            "Send a crew member to a neutral Location. "
            "Discard the top card of YOUR deck. "
            "If it is a Mission card: you take an Incident AND the Bot takes an Incident. "
            "Otherwise, gain 1 Glory. "
            "If this card is a Mission card, promote it to Duty Officer."
        ),
    },
    "BUSINESS": {
        "label": "Business",
        "action": (
            "Log the top card of the Bot deck. "
            "Gain a Weapon card (Cargo or Ship if unavailable). "
            "Resolve the top card of the Bot deck. "
            "Log this card."
        ),
    },
    "AMBASSADOR": {
        "label": "Ambassador",
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 2 Glory. "
            "You may return an Incident from your hand or discard pile. "
            "If this card is a Mission card, promote it to Duty Officer. "
            "Otherwise, log this card."
        ),
    },
}

# ── Action menus ──────────────────────────────────────────────────────────────
# deck_ops — operations the app can execute automatically as clickable buttons:
#   discard_top(count)  — discard N cards from top of draw deck
#   log_top             — log (permanently remove) top card of draw deck
#   log_current         — log the card that was just drawn
#   return_current      — shuffle current card back into draw deck
#   log_duty_officer    — log the current duty officer card
#   promote_duty_officer— promote current card to duty officer

NO_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Gain a Person card. "
            "Discard the top 3 cards of the Bot deck. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Deploy this Ship; it explores. "
            "If a Person card is in the Bot Discard pile, send a crew member to a neutral Location. "
            "If a Cargo card is in the Bot Discard pile, gain 1 Latinum."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "For each Person card in the Bot Discard pile, gain 1 Latinum. "
            "For each Ship card in the Bot Discard pile, send a crew member to a neutral Location."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "CARGO": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 2 Latinum. "
            "Gain a Business card (Person if unavailable). "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "PERSON": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 1 Latinum or 1 Dilithium (whichever total is lower). "
            "Send a crew member to a neutral Location. "
            "Promote this card to Duty Officer."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
            {"type": "promote_duty_officer", "label": "Promote to Duty Officer"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "Gain a Business card (Cargo if unavailable). "
            "Send a crew member to a neutral Location. "
            "If the Bot has 5+ Latinum: gain 1 Dilithium and take an Incident card."
        ),
        "deck_ops": [],
    },
    "ENCOUNTER": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain a Person card. "
            "Gain a Cargo card. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Log the top card of the Bot deck. "
            "Discard the top 2 cards of the Bot deck."
        ),
        "deck_ops": [
            {"type": "log_top", "label": "Log Top Card"},
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
}

WITH_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 1 Dilithium. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "log_top", "label": "Log Top Card"},
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Deploy this Ship; it engages. "
            "Send a crew member to a neutral Location. "
            "Gain 1 Glory."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "Gain a Business card (Person, Ship, or Ally if unavailable). "
            "If an Attack card is in the Bot Discard pile: gain 1 Glory and 1 Latinum. "
            "Log Duty Officer. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "CARGO": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 1 Latinum. "
            "Gain 1 Dilithium. "
            "Log Duty Officer. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_top", "label": "Log Top Card"},
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "PERSON": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 1 Latinum. "
            "Gain 1 Dilithium. "
            "Take a Ship card (Ally if unavailable)."
        ),
        "deck_ops": [
            {"type": "log_top", "label": "Log Top Card"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "If able to do BOTH: log a controlled Location and remove 2 crew members "
            "to take the top Encounter card, then log this card. "
            "Otherwise: gain a Cargo or Ship card."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card (if condition met)"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Gain 1 Dilithium. "
            "Gain 1 Glory. "
            "Take a Ship card (Ally if unavailable). "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Gain 1 Glory. "
            "Gain 1 Latinum. "
            "Log Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
        ],
    },
}

# ── Starting cards ─────────────────────────────────────────────────────────────
# Distribution from table: ALLY×2, CARGO×4, DIRECTIVE×6, LOCATION×2,
#   PERSON×3, SHIP×4, OTHER×2 = 23 deck cards + 1 captain = 24 total
# Starting positions: Available×10, Deployed×1, Reserve×5, Development×7
# Names are placeholders — replace with actual card names.

CARDS = [
    # Captain (set aside face-up, never enters a deck)
    {
        "id": "shran_captain",
        "name": "Shran",
        "card_type": "CAPTAIN",
        "traits": [],
        "starting_location": "captain",
    },

    # ── Available ×10 (shuffled → base of draw deck) ──────────────────────────
    {"id": "shran_ally_01",      "name": "[Ally 1]",      "card_type": "ALLY",      "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_ally_02",      "name": "[Ally 2]",      "card_type": "ALLY",      "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_cargo_01",     "name": "[Cargo 1]",     "card_type": "CARGO",     "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_cargo_02",     "name": "[Cargo 2]",     "card_type": "CARGO",     "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_directive_01", "name": "[Directive 1]", "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_directive_02", "name": "[Directive 2]", "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_directive_03", "name": "[Directive 3]", "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_person_01",    "name": "[Person 1]",    "card_type": "PERSON",    "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_person_02",    "name": "[Person 2]",    "card_type": "PERSON",    "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "shran_location_01",  "name": "[Location 1]", "card_type": "LOCATION",  "traits": [], "points": 0, "specialty": None, "starting_location": "available"},

    # ── Deployed ×1 (placed on top of draw deck after shuffling) ──────────────
    {"id": "shran_ship_01", "name": "[Ship 1 — Deployed]", "card_type": "SHIP", "traits": [], "points": 0, "specialty": None, "starting_location": "deployed"},

    # ── Reserve ×5 (shuffled → top layer of reserve deck) ────────────────────
    {"id": "shran_directive_04", "name": "[Directive 4]", "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "shran_cargo_03",     "name": "[Cargo 3]",     "card_type": "CARGO",     "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "shran_ship_02",      "name": "[Ship 2]",      "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "shran_person_03",    "name": "[Person 3]",    "card_type": "PERSON",    "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "shran_location_02",  "name": "[Location 2]", "card_type": "LOCATION",  "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},

    # ── Development ×7 (shuffled → bottom layer of reserve deck) ─────────────
    {"id": "shran_directive_05", "name": "[Directive 5]", "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "shran_directive_06", "name": "[Directive 6]", "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "shran_cargo_04",     "name": "[Cargo 4]",     "card_type": "CARGO",     "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "shran_ship_03",      "name": "[Ship 3]",      "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "shran_ship_04",      "name": "[Ship 4]",      "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "shran_other_01",     "name": "[Other 1]",     "card_type": "OTHER",     "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "shran_other_02",     "name": "[Other 2]",     "card_type": "OTHER",     "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
]

# Index for fast lookup
BY_ID = {c["id"]: c for c in CARDS}
