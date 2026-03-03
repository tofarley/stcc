"""
PICARD  (difficulty 1 of 10, CORE)
Starting deck: Available×10, Deployed×1, Reserve×4, Development×8
Symbol distribution: ALLY×1, CARGO×1, DIRECTIVE×8, INCIDENT×1, LOCATION×3, PERSON×6, SHIP×3
Total: 24 (Captain + 23 deck cards)
"""

CAPTAIN_INFO = {
    "id": "picard",
    "name": "Picard",
    "difficulty": "1 of 10",
    "set": "CORE",
}

TRAITS = {
    "SURPRISE": {
        "label": "Surprise",
        "action": "Resolve this card's Surprise operation.",
    },
    "SYNTHETIC": {
        "label": "Synthetic",
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 1 Dilithium. Gain 1 Glory. "
            "If this card is a Person, promote it to Duty Officer."
        ),
    },
    "ANDROID": {
        "label": "Android",
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "Send a crew member to a neutral Location. "
            "If able, return an Android card from discard. "
            "Otherwise, gain 1 Glory and take an Android card."
        ),
    },
    "ALIEN": {
        "label": "Alien",
        "action": (
            "Discard the top card of the Bot deck. "
            "Gain 1 Glory. "
            "If Bot has 5+ Latinum: gain 1 Glory and a Cargo card. "
            "Log this card."
        ),
    },
    "DOCTOR": {
        "label": "Doctor",
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "If able, return a Ship from discard. "
            "Otherwise, gain 2 Dilithium and 1 Glory. "
            "If this card is a Person, promote it to Duty Officer."
        ),
    },
    "ATTACK": {
        "label": "Attack",
        "action": (
            "Send a crew member to a neutral Location. "
            "If able, put a Ship from Bot Discard pile on top of the Bot deck. "
            "Otherwise, gain 1 Glory. "
            "If this card is a Person, promote it to Duty Officer."
        ),
    },
}

NO_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain a Person card. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "log_top",        "label": "Log Top Card"},
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Deploy this Ship; it explores. "
            "If a Person card is in Bot Discard pile, send a crew member to a neutral Location."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "For each Person card in Bot Discard pile, gain 1 Latinum. "
            "For each Ship card in Bot Discard pile, send a crew member to a neutral Location."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
    "CARGO": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 2 Dilithium. "
            "Take a Person card. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
            {"type": "log_current",  "label": "Log This Card"},
        ],
    },
    "PERSON": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 1 Dilithium / Latinum (whichever is lower). "
            "Send a crew member to a neutral Location. "
            "Promote this card to Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_top",              "label": "Log Top Card"},
            {"type": "promote_duty_officer",  "label": "Promote to Duty Officer"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "If able, gain a Klingon card. "
            "Otherwise, gain a Ship / Ally card and take an Incident. "
            "Gain 1 Dilithium / Latinum (whichever is lower). "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [],
    },
    "ENCOUNTER": {
        "action": (
            "Log the top 2 cards of the Bot deck. "
            "Take a Ship card. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_top",       "label": "Log Top Card"},
            {"type": "log_top",       "label": "Log 2nd Top Card"},
            {"type": "log_current",   "label": "Log This Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Log the top card of the Bot deck. "
            "Discard the top 3 cards of the Bot deck."
        ),
        "deck_ops": [
            {"type": "log_top",        "label": "Log Top Card"},
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
}

WITH_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 1 Dilithium. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Gain 1 Glory. "
            "Deploy this Ship; it explores. "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "Discard the top card of the Bot deck. "
            "Gain a Klingon card (Person, Ship, or Ally if unavailable). "
            "Log Duty Officer. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 1, "label": "Discard Top Card"},
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
            {"type": "log_current",      "label": "Log This Card"},
        ],
    },
    "CARGO": {
        "action": (
            "Log the top card of the Bot deck. "
            "Discard the top 2 cards of the Bot deck. "
            "Gain a Ship card. Deploy the gained Ship; it explores. "
            "Log Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_top",        "label": "Log Top Card"},
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
        ],
    },
    "PERSON": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 1 Dilithium / Latinum (whichever is lower). "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [
            {"type": "log_top", "label": "Log Top Card"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "If able to do BOTH: log a controlled Location and remove 2 crew members "
            "to take the top Encounter card, then log this card. "
            "Otherwise: gain a card (Alien or Cargo / Ally if unavailable)."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card (if condition met)"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Gain 1 Dilithium / Latinum (whichever is higher). "
            "Take a Klingon card (Ally or Ship if unavailable). "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Log the top 2 cards of the Bot deck. "
            "Gain 1 Dilithium. "
            "Log Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_top",          "label": "Log Top Card"},
            {"type": "log_top",          "label": "Log 2nd Top Card"},
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
        ],
    },
}

# Placeholder cards — fill in actual names.
# Distribution: ALLY×1, CARGO×1, DIRECTIVE×8, INCIDENT×1, LOCATION×3, PERSON×6, SHIP×3
CARDS = [
    {"id": "picard_captain",      "name": "Picard",          "card_type": "CAPTAIN",   "traits": [], "starting_location": "captain"},

    # Available ×10
    {"id": "picard_ally_01",      "name": "[Ally 1]",        "card_type": "ALLY",      "traits": [], "starting_location": "available"},
    {"id": "picard_cargo_01",     "name": "[Cargo 1]",       "card_type": "CARGO",     "traits": [], "starting_location": "available"},
    {"id": "picard_directive_01", "name": "[Directive 1]",   "card_type": "DIRECTIVE", "traits": [], "starting_location": "available"},
    {"id": "picard_directive_02", "name": "[Directive 2]",   "card_type": "DIRECTIVE", "traits": [], "starting_location": "available"},
    {"id": "picard_directive_03", "name": "[Directive 3]",   "card_type": "DIRECTIVE", "traits": [], "starting_location": "available"},
    {"id": "picard_person_01",    "name": "[Person 1]",      "card_type": "PERSON",    "traits": [], "starting_location": "available"},
    {"id": "picard_person_02",    "name": "[Person 2]",      "card_type": "PERSON",    "traits": [], "starting_location": "available"},
    {"id": "picard_person_03",    "name": "[Person 3]",      "card_type": "PERSON",    "traits": [], "starting_location": "available"},
    {"id": "picard_ship_01",      "name": "[Ship 1]",        "card_type": "SHIP",      "traits": [], "starting_location": "available"},
    {"id": "picard_location_01",  "name": "[Location 1]",   "card_type": "LOCATION",  "traits": [], "starting_location": "available"},

    # Deployed ×1
    {"id": "picard_ship_02",      "name": "[Ship 2 — Deployed]", "card_type": "SHIP", "traits": [], "starting_location": "deployed"},

    # Reserve ×4
    {"id": "picard_directive_04", "name": "[Directive 4]",   "card_type": "DIRECTIVE", "traits": [], "starting_location": "reserve"},
    {"id": "picard_directive_05", "name": "[Directive 5]",   "card_type": "DIRECTIVE", "traits": [], "starting_location": "reserve"},
    {"id": "picard_person_04",    "name": "[Person 4]",      "card_type": "PERSON",    "traits": [], "starting_location": "reserve"},
    {"id": "picard_location_02",  "name": "[Location 2]",   "card_type": "LOCATION",  "traits": [], "starting_location": "reserve"},

    # Development ×8
    {"id": "picard_directive_06", "name": "[Directive 6]",   "card_type": "DIRECTIVE", "traits": [], "starting_location": "development"},
    {"id": "picard_directive_07", "name": "[Directive 7]",   "card_type": "DIRECTIVE", "traits": [], "starting_location": "development"},
    {"id": "picard_directive_08", "name": "[Directive 8]",   "card_type": "DIRECTIVE", "traits": [], "starting_location": "development"},
    {"id": "picard_incident_01",  "name": "[Incident 1]",    "card_type": "INCIDENT",  "traits": [], "starting_location": "development"},
    {"id": "picard_location_03",  "name": "[Location 3]",   "card_type": "LOCATION",  "traits": [], "starting_location": "development"},
    {"id": "picard_person_05",    "name": "[Person 5]",      "card_type": "PERSON",    "traits": [], "starting_location": "development"},
    {"id": "picard_person_06",    "name": "[Person 6]",      "card_type": "PERSON",    "traits": [], "starting_location": "development"},
    {"id": "picard_ship_03",      "name": "[Ship 3]",        "card_type": "SHIP",      "traits": [], "starting_location": "development"},
]

BY_ID = {c["id"]: c for c in CARDS}
