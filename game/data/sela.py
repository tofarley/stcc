"""
SELA  (difficulty 5 of 10, CORE)
Starting deck: Available×7, Deployed×1, Reserve×6, Development×6, Discard×3
Symbol distribution: ALLY×1, CARGO×2, DIRECTIVE×5, LOCATION×1, PERSON×2, SHIP×7, OTHER×5
Total: 24 (Captain + 23 deck cards; 3 cards start in discard pile)
"""

CAPTAIN_INFO = {
    "id": "sela",
    "name": "Sela",
    "difficulty": "5 of 10",
    "set": "CORE",
}

# Specialty track thresholds — fill in actual values from rulebook.
SPECIALTY_THRESHOLDS = {
    "research":  [],
    "influence": [],
    "military":  [],
}

TRAITS = {
    "SURPRISE": {
        "label": "Surprise",
        "action": "Resolve this card's Surprise operation.",
    },
    "SHADY": {
        "label": "Shady",
        "action": (
            "Gain 1 Glory. "
            "If able, gain a Klingon > Ship card. "
            "If Bot has 8+ Glory: take control of the neutral Location with most Bot tokens "
            "(minimum 1) and log this card. "
            "If Bot has 7 or fewer Glory: gain 1 Glory and 1 Latinum."
        ),
    },
    "CLOAK": {
        "label": "Cloak",
        "action": (
            "If this card is a Ship: send a crew member to a neutral Location (ignoring any "
            "opponent Ship) and deploy this Ship; it engages. "
            "Otherwise: log this card and gain 3 Dilithium."
        ),
    },
    "VULCAN": {
        "label": "Vulcan",
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 1 Dilithium / Latinum (whichever is lower). "
            "Gain a Klingon > Ship card. "
            "If this card is a Person, promote it to Duty Officer."
        ),
    },
    "KLINGON": {
        "label": "Klingon",
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 2 Latinum / Glory (whichever is lower). "
            "If this card is a Ship: deploy this Ship; it explores. "
            "Otherwise: either you dismiss a Ship OR resolve the top card of the Bot deck."
        ),
    },
    "ATTACK": {
        "label": "Attack",
        "action": (
            "Junk the most valuable card in the Market (ignoring any with tokens). "
            "Send a crew member to a neutral Location. "
            "You take an Incident OR dismiss (one of) your Duty Officer(s). "
            "If Bot has 8+ Glory: log this card and either you log a controlled Location "
            "OR discard a card."
        ),
    },
}

NO_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Gain 1 Dilithium / Latinum / Glory (whichever is lower). "
            "Gain a Person / Ally card. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Gain 1 Glory. "
            "Deploy this Ship; it explores."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain a Klingon > Shady > Person card. "
            "Send a crew member to a neutral Location (ignoring any opponent Ship). "
            "You may draw a card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
    "CARGO": {
        "action": (
            "Gain an Ally > Person card. "
            "If Bot has 7+ Glory: gain 1 Dilithium and 1 Latinum. "
            "Otherwise: gain 2 Dilithium and 1 Glory."
        ),
        "deck_ops": [],
    },
    "PERSON": {
        "action": (
            "Gain 1 Glory. "
            "If able, gain a Vulcan > Klingon > Ship card (to gain a Person / Ship). "
            "Otherwise: gain a Cargo card. "
            "Promote this card to Duty Officer."
        ),
        "deck_ops": [
            {"type": "promote_duty_officer", "label": "Promote to Duty Officer"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "Gain 2 Dilithium / Latinum / Glory (whichever is lower)."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Resolve the top card of the Supplement deck. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain a Person card and promote it to Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_top", "label": "Log Top Card"},
        ],
    },
}

WITH_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 1 Glory. "
            "Send a crew member to a neutral Location. "
            "You may draw a card. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "log_top",        "label": "Log Top Card"},
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Deploy this Ship; it engages. "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Take an Incident. "
            "Gain 2 Dilithium / Latinum / Glory (whichever is lower), and you take an Incident. "
            "Dismiss Duty Officer. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2,   "label": "Discard Top 2 Cards"},
            {"type": "dismiss_duty_officer",       "label": "Dismiss Duty Officer"},
            {"type": "log_current",                "label": "Log This Card"},
        ],
    },
    "CARGO": {
        "action": (
            "Resolve the top card of the Supplement deck. "
            "Log Duty Officer. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
            {"type": "log_current",      "label": "Log This Card"},
        ],
    },
    "PERSON": {
        "action": (
            "Log the top card of the Bot deck. "
            "Discard the top 3 cards of the Bot deck. "
            "If able, gain a Shady > Vulcan card. "
            "Otherwise: gain 2 Dilithium."
        ),
        "deck_ops": [
            {"type": "log_top",        "label": "Log Top Card"},
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "If able, remove 2 crew members to gain the top Encounter card, "
            "then log this card and log Duty Officer. "
            "Otherwise: gain a Shady > Attack > Cargo / Ship card."
        ),
        "deck_ops": [
            {"type": "log_current",      "label": "Log This Card (if condition met)"},
            {"type": "log_duty_officer", "label": "Log Duty Officer (if condition met)"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Gain 2 Dilithium. "
            "Send a crew member to a neutral Location. "
            "Send a crew member to a neutral Location. "
            "Log Duty Officer. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
            {"type": "log_current",      "label": "Log This Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "If able, gain a Shady card. "
            "Otherwise: dismiss Duty Officer, gain a Person / Cargo / Ally card, "
            "and you discard a card."
        ),
        "deck_ops": [
            {"type": "dismiss_duty_officer", "label": "Dismiss Duty Officer (if unable to gain Shady)"},
        ],
    },
}

# Placeholder cards — fill in actual names.
# Distribution: ALLY×1, CARGO×2, DIRECTIVE×5, LOCATION×1, PERSON×2, SHIP×7, OTHER×5
# Note: 3 cards start in the discard pile.
CARDS = [
    {"id": "sela_captain",      "name": "Sela",             "card_type": "CAPTAIN",   "traits": [], "points": 0, "starting_location": "captain"},

    # Available ×7
    {"id": "sela_cargo_01",     "name": "[Cargo 1]",        "card_type": "CARGO",     "traits": [], "points": 0, "starting_location": "available"},
    {"id": "sela_directive_01", "name": "[Directive 1]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "starting_location": "available"},
    {"id": "sela_directive_02", "name": "[Directive 2]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "starting_location": "available"},
    {"id": "sela_ship_01",      "name": "[Ship 1]",         "card_type": "SHIP",      "traits": [], "points": 0, "starting_location": "available"},
    {"id": "sela_ship_02",      "name": "[Ship 2]",         "card_type": "SHIP",      "traits": [], "points": 0, "starting_location": "available"},
    {"id": "sela_ship_03",      "name": "[Ship 3]",         "card_type": "SHIP",      "traits": [], "points": 0, "starting_location": "available"},
    {"id": "sela_other_01",     "name": "[Other 1]",        "card_type": "OTHER",     "traits": [], "points": 0, "starting_location": "available"},

    # Deployed ×1
    {"id": "sela_ship_04",      "name": "[Ship 4 — Deployed]","card_type": "SHIP",    "traits": [], "points": 0, "starting_location": "deployed"},

    # Reserve ×6
    {"id": "sela_ally_01",      "name": "[Ally 1]",         "card_type": "ALLY",      "traits": [], "points": 0, "starting_location": "reserve"},
    {"id": "sela_directive_03", "name": "[Directive 3]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "starting_location": "reserve"},
    {"id": "sela_directive_04", "name": "[Directive 4]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "starting_location": "reserve"},
    {"id": "sela_ship_05",      "name": "[Ship 5]",         "card_type": "SHIP",      "traits": [], "points": 0, "starting_location": "reserve"},
    {"id": "sela_ship_06",      "name": "[Ship 6]",         "card_type": "SHIP",      "traits": [], "points": 0, "starting_location": "reserve"},
    {"id": "sela_other_02",     "name": "[Other 2]",        "card_type": "OTHER",     "traits": [], "points": 0, "starting_location": "reserve"},

    # Development ×6
    {"id": "sela_cargo_02",     "name": "[Cargo 2]",        "card_type": "CARGO",     "traits": [], "points": 0, "starting_location": "development"},
    {"id": "sela_directive_05", "name": "[Directive 5]",    "card_type": "DIRECTIVE", "traits": [], "points": 0, "starting_location": "development"},
    {"id": "sela_location_01",  "name": "[Location 1]",    "card_type": "LOCATION",  "traits": [], "points": 0, "starting_location": "development"},
    {"id": "sela_person_01",    "name": "[Person 1]",       "card_type": "PERSON",    "traits": [], "points": 0, "starting_location": "development"},
    {"id": "sela_ship_07",      "name": "[Ship 7]",         "card_type": "SHIP",      "traits": [], "points": 0, "starting_location": "development"},
    {"id": "sela_other_03",     "name": "[Other 3]",        "card_type": "OTHER",     "traits": [], "points": 0, "starting_location": "development"},

    # Discard ×3 (start in discard pile at game start)
    {"id": "sela_person_02",    "name": "[Person 2]",       "card_type": "PERSON",    "traits": [], "points": 0, "starting_location": "discard"},
    {"id": "sela_other_04",     "name": "[Other 4]",        "card_type": "OTHER",     "traits": [], "points": 0, "starting_location": "discard"},
    {"id": "sela_other_05",     "name": "[Other 5]",        "card_type": "OTHER",     "traits": [], "points": 0, "starting_location": "discard"},
]

BY_ID = {c["id"]: c for c in CARDS}
