"""
SISKO  (difficulty 4 of 10, CORE)
Starting deck: Available×10, Controlled Location×1, Deployed×1, Reserve×5, Development×7
Symbol distribution: ALLY×1, CARGO×2, DIRECTIVE×5, ENCOUNTER×1, INCIDENT×1,
                     LOCATION×3, PERSON×8, SHIP×3
Total: 25 (Captain + 24 deck cards)
"""

CAPTAIN_INFO = {
    "id": "sisko",
    "name": "Sisko",
    "difficulty": "4 of 10",
    "set": "CORE",
}

TRAITS = {
    "SURPRISE": {
        "label": "Surprise",
        "action": "Resolve this card's Surprise operation.",
    },
    "TRANSCENDENT": {
        "label": "Transcendent",
        "action": (
            "If able, gain a Bajoran card (Changeling if unavailable). "
            "Otherwise, gain 2 Glory and 1 Dilithium."
        ),
    },
    "STARBASE": {
        "label": "Starbase",
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "If this card is a Ship, deploy this card. "
            "Otherwise, gain 1 Dilithium. "
            "If able, resolve a Person from Bot Discard pile. "
            "Otherwise, gain 2 Latinum."
        ),
    },
    "BAJORAN": {
        "label": "Bajoran",
        "action": (
            "Gain 1 Latinum and 1 Glory. "
            "Take an Incident. "
            "If an Ally is in Bot Discard pile: send 2 crew members to a neutral Location. "
            "Otherwise: you dismiss (one of) your Duty Officer(s) and the Bot gains 2 Glory. "
            "If this card is a Person, promote it to Duty Officer."
        ),
    },
    "CHANGELING": {
        "label": "Changeling / Dominion",
        "action": (
            "Log the top card of the Bot deck. "
            "Resolve the top card of the Bot deck. "
            "If this card is a Person, promote it to Duty Officer."
        ),
    },
    "ATTACK": {
        "label": "Attack",
        "action": (
            "Send a crew member to a neutral Starbase > Starfleet > Location. "
            "If this card is a Ship: you discard a card and deploy this Ship; it engages. "
            "Otherwise, gain 2 Glory."
        ),
    },
}

NO_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Discard the top card of the Bot deck. "
            "Gain a Bajoran card (Changeling, Person, or Ally if unavailable). "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 1, "label": "Discard Top Card"},
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "Deploy this Ship; it explores. "
            "If a Person card is in Bot Discard pile, send a crew member to a neutral "
            "Starbase > Starfleet > Location."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "ALLY": {
        "action": (
            "Gain 1 Latinum. "
            "Discard the top 2 cards of the Bot deck. "
            "For each Person card in Bot Discard pile, gain 1 Dilithium. "
            "For each Ship card in Bot Discard pile, send a crew member to a neutral "
            "Starbase > Starfleet > Location."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
    "CARGO": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "If able, log a Person card from Bot Discard pile. "
            "Gain 1 Latinum. "
            "Gain 1 Glory. "
            "Gain a Bajoran / Starfleet card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
    "PERSON": {
        "action": (
            "Gain 1 Latinum. "
            "Send a crew member to a neutral Location. "
            "Promote this card to Duty Officer."
        ),
        "deck_ops": [
            {"type": "promote_duty_officer", "label": "Promote to Duty Officer"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "If able, log a Person from Bot Discard pile to send a crew member to a neutral Location. "
            "Otherwise, gain 1 Dilithium / Latinum (whichever is lower) and gain a Person card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "Take a Bajoran / Person card. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
            {"type": "log_current",             "label": "Log This Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Log the top card of the Bot deck. "
            "Discard the top 3 cards of the Bot deck. "
            "Gain 1 Glory. "
            "If able, return a Ship from Bot Discard pile to the top of the Bot deck."
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
            "Take a Bajoran > Ship > Cargo card. "
            "Gain 1 Glory. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "return_current", "label": "Return This Card to Deck"},
        ],
    },
    "SHIP": {
        "action": (
            "If able, log a Starbase card in play to resolve the top card of the Supplement deck. "
            "Deploy this Ship; it explores. "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [],
    },
    "ALLY": {
        "action": (
            "Gain 1 Latinum / Glory (whichever is lower). "
            "Gain a Cargo > Ship / Ally card. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "CARGO": {
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "Gain 1 Glory. "
            "Gain a Bajoran > Starfleet > Ship card. "
            "Log Duty Officer."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
            {"type": "log_duty_officer",        "label": "Log Duty Officer"},
        ],
    },
    "PERSON": {
        "action": (
            "Discard the top 3 cards of the Bot deck. "
            "Gain 1 Dilithium / Glory (whichever is lower). "
            "Gain a Ship / Ally card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "If able to do BOTH: log a controlled Location (not a Starbase) and remove 2 crew "
            "members to take the top Encounter card, then log this card. "
            "Otherwise: send a crew member to a neutral Location, gain 1 Latinum, "
            "and dismiss Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_current",          "label": "Log This Card (if condition met)"},
            {"type": "dismiss_duty_officer", "label": "Dismiss Duty Officer (otherwise)"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Discard the top card of the Bot deck. "
            "Gain 1 Glory. "
            "Gain 1 Latinum. "
            "Take a Ship / Ally card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 1, "label": "Discard Top Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Log the top card of the Bot deck. "
            "Discard the top 3 cards of the Bot deck. "
            "Gain 1 Latinum. "
            "Log Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_top",          "label": "Log Top Card"},
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
        ],
    },
}

# Placeholder cards — fill in actual names.
# Distribution: ALLY×1, CARGO×2, DIRECTIVE×5, ENCOUNTER×1, INCIDENT×1,
#               LOCATION×3, PERSON×8, SHIP×3
CARDS = [
    {"id": "sisko_captain",      "name": "Sisko",              "card_type": "CAPTAIN",   "traits": [], "starting_location": "captain"},

    # Available ×10
    {"id": "sisko_ally_01",      "name": "[Ally 1]",           "card_type": "ALLY",      "traits": [], "starting_location": "available"},
    {"id": "sisko_cargo_01",     "name": "[Cargo 1]",          "card_type": "CARGO",     "traits": [], "starting_location": "available"},
    {"id": "sisko_directive_01", "name": "[Directive 1]",      "card_type": "DIRECTIVE", "traits": [], "starting_location": "available"},
    {"id": "sisko_directive_02", "name": "[Directive 2]",      "card_type": "DIRECTIVE", "traits": [], "starting_location": "available"},
    {"id": "sisko_person_01",    "name": "[Person 1]",         "card_type": "PERSON",    "traits": [], "starting_location": "available"},
    {"id": "sisko_person_02",    "name": "[Person 2]",         "card_type": "PERSON",    "traits": [], "starting_location": "available"},
    {"id": "sisko_person_03",    "name": "[Person 3]",         "card_type": "PERSON",    "traits": [], "starting_location": "available"},
    {"id": "sisko_person_04",    "name": "[Person 4]",         "card_type": "PERSON",    "traits": [], "starting_location": "available"},
    {"id": "sisko_ship_01",      "name": "[Ship 1]",           "card_type": "SHIP",      "traits": [], "starting_location": "available"},
    {"id": "sisko_location_01",  "name": "[Location 1]",      "card_type": "LOCATION",  "traits": [], "starting_location": "available"},

    # Controlled Location ×1 (shuffled with deployed, placed on top of draw deck)
    {"id": "sisko_location_02",  "name": "[Location 2 — Controlled]", "card_type": "LOCATION", "traits": [], "starting_location": "controlled_location"},

    # Deployed ×1
    {"id": "sisko_ship_02",      "name": "[Ship 2 — Deployed]","card_type": "SHIP",      "traits": [], "starting_location": "deployed"},

    # Reserve ×5
    {"id": "sisko_cargo_02",     "name": "[Cargo 2]",          "card_type": "CARGO",     "traits": [], "starting_location": "reserve"},
    {"id": "sisko_directive_03", "name": "[Directive 3]",      "card_type": "DIRECTIVE", "traits": [], "starting_location": "reserve"},
    {"id": "sisko_directive_04", "name": "[Directive 4]",      "card_type": "DIRECTIVE", "traits": [], "starting_location": "reserve"},
    {"id": "sisko_person_05",    "name": "[Person 5]",         "card_type": "PERSON",    "traits": [], "starting_location": "reserve"},
    {"id": "sisko_person_06",    "name": "[Person 6]",         "card_type": "PERSON",    "traits": [], "starting_location": "reserve"},

    # Development ×7
    {"id": "sisko_directive_05", "name": "[Directive 5]",      "card_type": "DIRECTIVE", "traits": [], "starting_location": "development"},
    {"id": "sisko_encounter_01", "name": "[Encounter 1]",      "card_type": "ENCOUNTER", "traits": [], "starting_location": "development"},
    {"id": "sisko_incident_01",  "name": "[Incident 1]",       "card_type": "INCIDENT",  "traits": [], "starting_location": "development"},
    {"id": "sisko_location_03",  "name": "[Location 3]",      "card_type": "LOCATION",  "traits": [], "starting_location": "development"},
    {"id": "sisko_person_07",    "name": "[Person 7]",         "card_type": "PERSON",    "traits": [], "starting_location": "development"},
    {"id": "sisko_person_08",    "name": "[Person 8]",         "card_type": "PERSON",    "traits": [], "starting_location": "development"},
    {"id": "sisko_ship_03",      "name": "[Ship 3]",           "card_type": "SHIP",      "traits": [], "starting_location": "development"},
]

BY_ID = {c["id"]: c for c in CARDS}
