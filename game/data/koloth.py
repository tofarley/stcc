"""
KOLOTH  (difficulty 3 of 10, CORE)
Starting deck: Available×10, Deployed×1, Reserve×5, Development×7
Symbol distribution: CARGO×3, DIRECTIVE×5, LOCATION×2, PERSON×3, SHIP×7, OTHER×3
Total: 24 (Captain + 23 deck cards)
"""

CAPTAIN_INFO = {
    "id": "koloth",
    "name": "Koloth",
    "difficulty": "3 of 10",
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
        {"at": 3,  "multiplier": 2},
        {"at": 8,  "multiplier": 3},
        {"at": 11, "multiplier": 5},
        {"at": 15, "multiplier": 7},
    ],
    "military": [
        {"at": 0,  "multiplier": 1},
        {"at": 2,  "multiplier": 2},
        {"at": 7,  "multiplier": 3},
        {"at": 10, "multiplier": 4},
        {"at": 13, "multiplier": 5},
        {"at": 15, "multiplier": 7},
    ],
}

TRAITS = {
    "SURPRISE": {
        "label": "Surprise",
        "action": "Resolve this card's Surprise operation.",
    },
    "WEAPON": {
        "label": "Weapon",
        "action": (
            "Junk the most valuable card in the Market (ignoring any with tokens). "
            "Gain 1 Glory. "
            "If Bot has 9+ Latinum AND Bot Duty Officer is a Klingon: dismiss Duty Officer, "
            "gain 4 Dilithium, and log this card. "
            "Otherwise, if able, remove a token. "
            "Otherwise, gain 1 Glory."
        ),
    },
    "ATTACK": {
        "label": "Attack",
        "action": (
            "Junk the most valuable card in the Market (ignoring any with tokens). "
            "If able, return a Ship from discard to the top of the Bot deck. "
            "If Bot Duty Officer is a Klingon: dismiss Duty Officer and gain 4 Dilithium. "
            "Otherwise, if able, dismiss a Ship. "
            "Otherwise, gain 1 Glory."
        ),
    },
    "ROMULAN": {
        "label": "Romulan",
        "action": (
            "Log the top card of the Bot deck. "
            "Take the top card of the Supplement deck. "
            "Log this card."
        ),
    },
    "SCIENTIST": {
        "label": "Scientist",
        "action": (
            "Discard the top card of the Bot deck. "
            "Gain 2 Latinum. "
            "Gain 1 Dilithium."
        ),
    },
}

NO_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Gain a Romulan / Person / Ship card. "
            "Send a crew member to a neutral Location. "
            "You may draw a card. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Deploy this Ship; it explores. "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "If able, gain a Romulan card. "
            "Otherwise, take a Ship / Person card AND you take an Incident. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "CARGO": {
        "action": (
            "Gain 1 Latinum. "
            "Gain 1 Glory. "
            "Gain a Person / Ship / Ally card."
        ),
        "deck_ops": [],
    },
    "PERSON": {
        "action": (
            "Discard the top card of the Bot deck. "
            "Log the top card of the Bot deck. "
            "Gain 1 Glory / Latinum (whichever is lower). "
            "Gain a Weapon card (Ship if unavailable). "
            "Promote this card to Duty Officer."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 1, "label": "Discard Top Card"},
            {"type": "log_top",              "label": "Log Top Card"},
            {"type": "promote_duty_officer", "label": "Promote to Duty Officer"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "Gain 1 Glory. "
            "Take an Incident card. "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Gain a Person / Ally card. "
            "Send a crew member to a neutral Location. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Log the top card of the Bot deck. "
            "Discard the top 2 cards of the Bot deck. "
            "If a Ship card is in Bot Discard pile, gain 1 Dilithium."
        ),
        "deck_ops": [
            {"type": "log_top",        "label": "Log Top Card"},
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
}

WITH_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Gain 1 Glory. "
            "If able, gain a Romulan card. "
            "Otherwise, take a Ship > Cargo card. "
            "Send a crew member to a neutral Location. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Gain 1 Dilithium. "
            "Deploy this Ship; it engages. "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "If able, gain a Romulan card. "
            "Otherwise: take an Incident, gain 1 Dilithium, you take an Incident and discard it, "
            "then dismiss Duty Officer. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "dismiss_duty_officer", "label": "Dismiss Duty Officer (if condition)"},
            {"type": "log_current",          "label": "Log This Card"},
        ],
    },
    "CARGO": {
        "action": (
            "Gain 1 Latinum. "
            "Gain 1 Glory. "
            "Discard the top card of the Supplement deck. "
            "Log Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
        ],
    },
    "PERSON": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain a Cargo card. "
            "If able, return a Ship from Bot Discard pile to the top of the Bot deck. "
            "Otherwise, take a Ship card."
        ),
        "deck_ops": [
            {"type": "log_top", "label": "Log Top Card"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "If able to do BOTH: log a Ship card and remove a crew member to take the top "
            "Encounter card, then log this card and log Duty Officer. "
            "Otherwise: gain 1 Dilithium, 1 Glory, and a Person card."
        ),
        "deck_ops": [
            {"type": "log_duty_officer", "label": "Log Duty Officer (if condition met)"},
            {"type": "log_current",      "label": "Log This Card (if condition met)"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Gain 1 Latinum / Dilithium (whichever is higher). "
            "Gain a Ship card. "
            "Deploy the gained Ship; it engages."
        ),
        "deck_ops": [],
    },
    "LOCATION": {
        "action": (
            "Dismiss Duty Officer. "
            "Gain 1 Dilithium. "
            "Resolve the top card of the Bot deck."
        ),
        "deck_ops": [
            {"type": "dismiss_duty_officer", "label": "Dismiss Duty Officer"},
        ],
    },
}

# Placeholder cards — fill in actual names.
# Distribution: CARGO×3, DIRECTIVE×5, LOCATION×2, PERSON×3, SHIP×7, OTHER×3
CARDS = [
    {"id": "koloth_captain",      "name": "Koloth",           "card_type": "CAPTAIN",   "traits": [], "points": 0, "specialty": None, "starting_location": "captain"},

    # Available ×10
    {"id": "koloth_cargo_01",     "name": "[Cargo 1]",        "card_type": "CARGO",     "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_directive_01", "name": "[Directive 1]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_directive_02", "name": "[Directive 2]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_person_01",    "name": "[Person 1]",       "card_type": "PERSON",    "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_person_02",    "name": "[Person 2]",       "card_type": "PERSON",    "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_ship_01",      "name": "[Ship 1]",         "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_ship_02",      "name": "[Ship 2]",         "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_ship_03",      "name": "[Ship 3]",         "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_ship_04",      "name": "[Ship 4]",         "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "koloth_other_01",     "name": "[Other 1]",        "card_type": "OTHER",     "traits": [], "points": 0, "specialty": None, "starting_location": "available"},

    # Deployed ×1
    {"id": "koloth_ship_05",      "name": "[Ship 5 — Deployed]","card_type": "SHIP",    "traits": [], "points": 0, "specialty": None, "starting_location": "deployed"},

    # Reserve ×5
    {"id": "koloth_cargo_02",     "name": "[Cargo 2]",        "card_type": "CARGO",     "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "koloth_directive_03", "name": "[Directive 3]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "koloth_directive_04", "name": "[Directive 4]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "koloth_location_01",  "name": "[Location 1]",    "card_type": "LOCATION",  "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "koloth_person_03",    "name": "[Person 3]",       "card_type": "PERSON",    "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},

    # Development ×7
    {"id": "koloth_cargo_03",     "name": "[Cargo 3]",        "card_type": "CARGO",     "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "koloth_directive_05", "name": "[Directive 5]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "koloth_location_02",  "name": "[Location 2]",    "card_type": "LOCATION",  "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "koloth_ship_06",      "name": "[Ship 6]",         "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "koloth_ship_07",      "name": "[Ship 7]",         "card_type": "SHIP",      "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "koloth_other_02",     "name": "[Other 2]",        "card_type": "OTHER",     "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "koloth_other_03",     "name": "[Other 3]",        "card_type": "OTHER",     "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
]

BY_ID = {c["id"]: c for c in CARDS}
