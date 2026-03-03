"""
BURNHAM  (difficulty 7 of 10, CORE)
Starting deck: Available×10, Deployed×1, Reserve×4, Development×8
Special starting cards: Status×1 (set aside), Incident Deck×1 (incident pile)
Symbol distribution: CARGO×2, DIRECTIVE×4, LOCATION×3, PERSON×11, SHIP×3
  (Status and Captain counted separately; Incident card is in incident pile)
Total: 26 cards (Captain + Status + Incident + 23 deck cards)

Special rule: During the Clean-up Step, instead of adding a Stardate token, remove
1 Stardate token from the Stardate card and add 2 Dilithium to one Market card instead.
At the end of the game, the Bot scores 1 Glory per Dilithium token
(instead of the usual 1 Glory per 2 Dilithium).
"""

CAPTAIN_INFO = {
    "id": "burnham",
    "name": "Burnham",
    "difficulty": "7 of 10",
    "set": "CORE",
    "special_rule": (
        "Clean-up Step: instead of adding a Stardate token, remove 1 Stardate token and "
        "add 2 Dilithium to one Market card. "
        "End of game: Bot scores 1 Glory per Dilithium (not the usual 1 per 2)."
    ),
}

# Each entry is a list of {"at": N, "multiplier": M} steps in ascending order.
# The active multiplier is the highest step whose "at" value ≤ current track value.
SPECIALTY_THRESHOLDS = {
    "research": [
        {"at": 0,  "multiplier": 1},
        {"at": 2,  "multiplier": 2},
        {"at": 7,  "multiplier": 3},
        {"at": 10, "multiplier": 4},
        {"at": 13, "multiplier": 5},
        {"at": 15, "multiplier": 6},
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
        {"at": 5,  "multiplier": 3},
        {"at": 10, "multiplier": 4},
        {"at": 14, "multiplier": 5},
    ],
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
    "CREATURE": {
        "label": "Creature",
        "action": (
            "Gain 1 Glory. "
            "Gain a Person / Cargo card. "
            "If a Ship card is in Bot Discard pile, deploy it; it explores."
        ),
    },
    "SCIENTIST": {
        "label": "Scientist",
        "action": (
            "Log the top card of the Bot deck. "
            "Take an Incident card. "
            "Gain 1 Dilithium. "
            "Gain an Ally card."
        ),
    },
    "ANOMALY": {
        "label": "Anomaly",
        "action": (
            "If a Person card is in Bot Discard pile, promote it to Duty Officer. "
            "If this card is a Ship, deploy it; it explores. "
            "Otherwise, gain 2 Dilithium."
        ),
    },
    "KELPIEN": {
        "label": "Kelpien",
        "action": (
            "If able, gain a Kelpien card. "
            "Otherwise, gain the card in the Market with the most Latinum "
            "(most Dilithium if tied). "
            "If this card is a Person, promote it to Duty Officer."
        ),
    },
}

NO_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Discard the top card of the Bot deck. "
            "Gain 1 Dilithium. "
            "Gain a Scientist > Creature > Person card. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 1, "label": "Discard Top Card"},
            {"type": "return_current",           "label": "Return This Card to Deck"},
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
            "Discard the top 3 cards of the Bot deck. "
            "Take an Incident card. "
            "Gain 1 Dilithium."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "CARGO": {
        "action": (
            "Gain the card in the Market with the most Latinum (most Dilithium if tied). "
            "Send a crew member to a neutral Location. "
            "Log this card."
        ),
        "deck_ops": [
            {"type": "log_current", "label": "Log This Card"},
        ],
    },
    "PERSON": {
        "action": (
            "Gain 1 Dilithium. "
            "Send a crew member to a neutral Location. "
            "Promote this card to Duty Officer."
        ),
        "deck_ops": [
            {"type": "promote_duty_officer", "label": "Promote to Duty Officer"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 2 Dilithium. "
            "Remove 1 Stardate token from the Stardate card."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Log the top 2 cards of the Bot deck. "
            "Take a Person card."
        ),
        "deck_ops": [
            {"type": "log_top", "label": "Log Top Card"},
            {"type": "log_top", "label": "Log 2nd Top Card"},
        ],
    },
    "LOCATION": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 1 Glory. "
            "Gain 1 Dilithium / Latinum (whichever is lower)."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
}

WITH_DUTY_OFFICER = {
    "INCIDENT": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain 2 Dilithium. "
            "Send a crew member to a neutral Location. "
            "Return this card to the Bot deck."
        ),
        "deck_ops": [
            {"type": "log_top",        "label": "Log Top Card"},
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
            "Discard the top 3 cards of the Bot deck. "
            "Gain 1 Glory. "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 3, "label": "Discard Top 3 Cards"},
        ],
    },
    "CARGO": {
        "action": (
            "Log the top card of the Bot deck. "
            "Gain a Ship card. "
            "Log Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_top",          "label": "Log Top Card"},
            {"type": "log_duty_officer", "label": "Log Duty Officer"},
        ],
    },
    "PERSON": {
        "action": (
            "Discard the top 2 cards of the Bot deck. "
            "Gain 1 Dilithium / Latinum (whichever is lower). "
            "Send a crew member to a neutral Location."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards"},
        ],
    },
    "DIRECTIVE": {
        "action": (
            "If able to do BOTH: log a controlled Location and remove a crew member "
            "to gain the top Encounter card. "
            "Otherwise: discard the top 2 cards of the Bot deck and gain the card in the "
            "Market with the most Latinum (most Dilithium if tied)."
        ),
        "deck_ops": [
            {"type": "discard_top", "count": 2, "label": "Discard Top 2 Cards (otherwise)"},
        ],
    },
    "ENCOUNTER": {
        "action": (
            "Gain 1 Dilithium. "
            "Gain 1 Latinum. "
            "Gain a Scientist card (Anomaly or Ship if unavailable). "
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
            "Dismiss Duty Officer."
        ),
        "deck_ops": [
            {"type": "log_top",              "label": "Log Top Card"},
            {"type": "log_top",              "label": "Log 2nd Top Card"},
            {"type": "dismiss_duty_officer", "label": "Dismiss Duty Officer"},
        ],
    },
}

# Placeholder cards — fill in actual names.
# Deck cards (23): CARGO×2, DIRECTIVE×4, LOCATION×3, PERSON×11, SHIP×3
# Also: Captain (set aside), Status×1 (set aside), Incident×1 (incident pile)
CARDS = [
    {"id": "burnham_captain",      "name": "Burnham",                "card_type": "CAPTAIN",  "traits": [], "points": 0, "specialty": None, "starting_location": "captain"},
    {"id": "burnham_status_01",    "name": "[Status Card]",          "card_type": "OTHER",    "traits": [], "points": 0, "specialty": None, "starting_location": "status"},
    {"id": "burnham_incident_01",  "name": "[Incident Deck Card]",   "card_type": "INCIDENT", "traits": [], "points": 0, "specialty": None, "starting_location": "incident_deck"},

    # Available ×10
    {"id": "burnham_person_01",    "name": "[Person 1]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_person_02",    "name": "[Person 2]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_person_03",    "name": "[Person 3]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_person_04",    "name": "[Person 4]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_directive_01", "name": "[Directive 1]",          "card_type": "DIRECTIVE","traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_directive_02", "name": "[Directive 2]",          "card_type": "DIRECTIVE","traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_cargo_01",     "name": "[Cargo 1]",              "card_type": "CARGO",    "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_ship_01",      "name": "[Ship 1]",               "card_type": "SHIP",     "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_ship_02",      "name": "[Ship 2]",               "card_type": "SHIP",     "traits": [], "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "burnham_location_01",  "name": "[Location 1]",          "card_type": "LOCATION", "traits": [], "points": 0, "specialty": None, "starting_location": "available"},

    # Deployed ×1
    {"id": "burnham_ship_03",      "name": "[Ship 3 — Deployed]",   "card_type": "SHIP",     "traits": [], "points": 0, "specialty": None, "starting_location": "deployed"},

    # Reserve ×4
    {"id": "burnham_person_05",    "name": "[Person 5]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "burnham_person_06",    "name": "[Person 6]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "burnham_person_07",    "name": "[Person 7]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "burnham_location_02",  "name": "[Location 2]",          "card_type": "LOCATION", "traits": [], "points": 0, "specialty": None, "starting_location": "reserve"},

    # Development ×8
    {"id": "burnham_person_08",    "name": "[Person 8]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "burnham_person_09",    "name": "[Person 9]",             "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "burnham_person_10",    "name": "[Person 10]",            "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "burnham_person_11",    "name": "[Person 11]",            "card_type": "PERSON",   "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "burnham_directive_03", "name": "[Directive 3]",          "card_type": "DIRECTIVE","traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "burnham_directive_04", "name": "[Directive 4]",          "card_type": "DIRECTIVE","traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "burnham_location_03",  "name": "[Location 3]",          "card_type": "LOCATION", "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "burnham_cargo_02",     "name": "[Cargo 2]",              "card_type": "CARGO",    "traits": [], "points": 0, "specialty": None, "starting_location": "development"},
]

BY_ID = {c["id"]: c for c in CARDS}
