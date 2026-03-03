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
        {"at": 3,  "multiplier": 2},
        {"at": 8,  "multiplier": 3},
        {"at": 11, "multiplier": 5},
        {"at": 15, "multiplier": 7},
    ],
    "military": [
        {"at": 0,  "multiplier": 1},
        {"at": 5,  "multiplier": 3},
        {"at": 10, "multiplier": 4},
        {"at": 14, "multiplier": 5},
    ],
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

# Distribution: ALLY×1, CARGO×1, DIRECTIVE×8, INCIDENT×1, LOCATION×3, PERSON×6, SHIP×3
CARDS = [
    {"id": "picard_captain",           "name": "Picard",               "card_type": "CAPTAIN",   "traits": [],                                              "points": 0, "specialty": None, "starting_location": "captain"},

    # Available ×10
    {"id": "picard_loc_farpoint",      "name": "Farpoint Station",     "card_type": "LOCATION",  "traits": ["BUSINESS", "ANOMOLY"],                         "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_dir_snw",           "name": "Strange New Worlds",   "card_type": "DIRECTIVE", "traits": [],                                              "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_dir_diplomacy",     "name": "Diplomacy",            "card_type": "DIRECTIVE", "traits": [],                                              "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_per_worf",          "name": "Worf",                 "card_type": "PERSON",    "traits": ["STARFLEET", "SECURITY", "KLINGON", "ATTACK"],   "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_per_riker",         "name": "Will Riker",           "card_type": "PERSON",    "traits": ["STARFLEET", "HUMAN"],                          "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_dir_set_a_course",  "name": "Set a Course",         "card_type": "DIRECTIVE", "traits": [],                                              "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_dir_utilize",       "name": "Utilize Resources",    "card_type": "DIRECTIVE", "traits": [],                                              "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_inc_red_alert",     "name": "Red Alert",            "card_type": "INCIDENT",  "traits": [],                                              "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_dir_recruit",       "name": "Recruit",              "card_type": "DIRECTIVE", "traits": [],                                              "points": 0, "specialty": None, "starting_location": "available"},
    {"id": "picard_dir_analyze",       "name": "Analyze",              "card_type": "DIRECTIVE", "traits": [],                                              "points": 0, "specialty": None, "starting_location": "available"},

    # Deployed ×1
    {"id": "picard_ship_enterprise_d", "name": "U.S.S. Enterprise-D", "card_type": "SHIP",      "traits": ["STARFLEET"],                                   "points": 0, "specialty": None, "starting_location": "deployed"},

    # Reserve ×4
    {"id": "picard_per_data",          "name": "Data",                 "card_type": "PERSON",    "traits": ["STARFLEET", "ANDROID", "SYNTHETIC", "OPS"],    "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "picard_ship_type7",        "name": "Type 7 Shuttlecraft",  "card_type": "SHIP",      "traits": ["STARFLEET"],                                   "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "picard_per_crusher",       "name": "Beverly Crusher",      "card_type": "PERSON",    "traits": ["STARFLEET", "HUMAN", "DOCTOR"],                "points": 0, "specialty": None, "starting_location": "reserve"},
    {"id": "picard_dir_first_contact", "name": "First Contact",        "card_type": "DIRECTIVE", "traits": [],                                              "points": 0, "specialty": None, "starting_location": "reserve"},

    # Development ×8
    {"id": "picard_per_troi",          "name": "Deanna Troi",          "card_type": "PERSON",    "traits": ["STARFLEET", "BETAZOID", "TELEPATH", "HUMAN"],  "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "picard_cargo_phasing",     "name": "Phasing Cloak",        "card_type": "CARGO",     "traits": ["STARFLEET", "ONGOING", "WEAPON", "CLOAK"],     "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "picard_loc_starbase74",    "name": "Starbase 74",          "card_type": "LOCATION",  "traits": ["STARFLEET", "STARBASE"],                       "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "picard_dir_make_it_so",    "name": "Make It So",           "card_type": "DIRECTIVE", "traits": [],                                              "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "picard_loc_daystrom",      "name": "Daystrom Institute",   "card_type": "LOCATION",  "traits": ["STARFLEET", "ANDROID"],                        "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "picard_per_laforge",       "name": "Geordi LaForge",       "card_type": "PERSON",    "traits": ["STARFLEET", "HUMAN", "ENGINEER", "PILOT"],     "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "picard_ship_bozeman",      "name": "U.S.S. Bozeman",       "card_type": "SHIP",      "traits": ["TIME TRAVEL", "STARFLEET", "ANOMOLY"],         "points": 0, "specialty": None, "starting_location": "development"},
    {"id": "picard_ally_tamarians",    "name": "Tamarians",            "card_type": "ALLY",      "traits": ["ALIEN"],                                       "points": 0, "specialty": None, "starting_location": "development"},
]

BY_ID = {c["id"]: c for c in CARDS}
