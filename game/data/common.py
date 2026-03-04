# Common card pool — shared across all captains.
# Symbols on each card will be filled in by the user; placeholders marked with [].
# card_type matches the section the card is gained from / the primary symbol it contributes.

# _SPECIALTY_TRACKS = {"research", "influence", "military"}

CARDS = [
    # ── ALLY ──────────────────────────────────────────────────────────────────
    {"id": "c_ally_arinson",       "name": "Arin'Sen",       "card_type": "ALLY", "points": 3, "specialty": None,        "traits": ["KLINGON"]},
    {"id": "c_ally_bolians",       "name": "Bolians",        "card_type": "ALLY", "points": 3, "specialty": None,        "traits": []},
    {"id": "c_ally_bynars",        "name": "Bynars",         "card_type": "ALLY", "points": 3, "specialty": None,        "traits": ["ENGINEER", "ALIEN"]},
    {"id": "c_ally_denobulans",    "name": "Denobulans",     "card_type": "ALLY", "points": 3, "specialty": None,        "traits": []},
    {"id": "c_ally_edosians",      "name": "Edosians",       "card_type": "ALLY", "points": 3, "specialty": None,        "traits": ["ALIEN"]},
    {"id": "c_ally_emerald_chain", "name": "Emerald Chain",  "card_type": "ALLY", "points": 3, "specialty": None,        "traits": ["ANDORIAN", "ATTACK", "ORION", "SHADY"]},
    {"id": "c_ally_halkan",        "name": "Halkan Council", "card_type": "ALLY", "points": 3, "specialty": None,        "traits": []},
    {"id": "c_ally_karemma",       "name": "Karemma",        "card_type": "ALLY", "points": 3, "specialty": None,        "traits": ["BUSINESS", "DOMINION"]},
    {"id": "c_ally_kelpiens",      "name": "Kelpiens",       "card_type": "ALLY", "points": 0, "specialty": "research",  "traits": ["KELPIEN"]},
    {"id": "c_ally_letheans",      "name": "Letheans",       "card_type": "ALLY", "points": 0, "specialty": "military",  "traits": ["TELEPATH", "ATTACK", "SHADY"]},
    {"id": "c_ally_organians",     "name": "Organians",      "card_type": "ALLY", "points": 3, "specialty": None,        "traits": ["TRANSCENDENT", "ANOMOLY"]},
    {"id": "c_ally_suliban",       "name": "Suliban",        "card_type": "ALLY", "points": 0, "specialty": "influence", "traits": ["TIME TRAVEL", "ALIEN"]},
    {"id": "c_ally_tholians",      "name": "Tholians",       "card_type": "ALLY", "points": 3, "specialty": None,        "traits": ["ALIEN"]},

    # ── CARGO ─────────────────────────────────────────────────────────────────
    {"id": "c_cargo_biobed" ,         "name": "Biobed",                    "card_type": "CARGO", "points": 0, "specialty": "research",  "traits": ["DOCTOR"]},
    {"id": "c_cargo_borg_spatial",    "name": "Borg Spatial Trajector",    "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["SCIENTIST", "BORG"]},
    {"id": "c_cargo_cloaking",        "name": "Cloaking Device",           "card_type": "CARGO", "points": 0, "specialty": "military",  "traits": ["ONGOING", "CLOAK"]},
    {"id": "c_cargo_ferengi_wine",    "name": "Ferengi Wine",              "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["BEVERAGE", "FERENGI"]},
    {"id": "c_cargo_forced_sing",     "name": "Forced Singularity",        "card_type": "CARGO", "points": 0, "specialty": "research",  "traits": ["ROMULAN", "ANOMOLY", "ONGOING"]},
    {"id": "c_cargo_holosuite",       "name": "Holosuite",                 "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["HOLOGRAM", "BUSINESS"]},
    {"id": "c_cargo_horta",           "name": "Horta",                     "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["CREATURE", "ONGOING", "ALIEN"]},
    {"id": "c_cargo_lirpa",           "name": "Lirpa",                     "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["VULCAN", "WEAPON", "ATTACK"]},
    {"id": "c_cargo_mekleth",         "name": "Mek'Leth",                  "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["KLINGON", "WEAPON", "ATTACK"]},
    {"id": "c_cargo_orb_of_time",     "name": "Orb of Time",               "card_type": "CARGO", "points": 0, "specialty": "influence", "traits": ["TIME TRAVEL", "BAJORAN"]},
    {"id": "c_cargo_phasers",         "name": "Phasers",                   "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["STARFLEET", "SECURITY", "ONGOING", "WEAPON"]},
    {"id": "c_cargo_plasma_manifold", "name": "Plasma Manifold",           "card_type": "CARGO", "points": 0, "specialty": "military",  "traits": ["ENGINEER"]},
    {"id": "c_cargo_tachyon",         "name": "Tachyon Detection Grid",    "card_type": "CARGO", "points": 0, "specialty": "influence", "traits": ["COMMUNICATION", "ATTACK"]},
    {"id": "c_cargo_tribbles",        "name": "Tribbles",                  "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["CREATURE", "ATTACK"]},
    {"id": "c_cargo_type10",          "name": "Type III Disruptor Pistol", "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["WEAPON", "ATTACK"]},
    {"id": "c_cargo_unstable_wh",     "name": "Unstable Wormhole",         "card_type": "CARGO", "points": 2, "specialty": None,        "traits": ["ANOMALY"]},
  
    # ── LOCATION ──────────────────────────────────────────────────────────────
    {"id": "c_loc_amargosa",     "name": "Amargosa Observatory", "card_type": "LOCATION", "points": 3, "specialty": None,        "traits": ["SCIENTIST", "STARBASE"]},
    {"id": "c_loc_relay",        "name": "Ancient Relay Station","card_type": "LOCATION", "points": 0, "specialty": None,        "traits": ["COMMUNICATION", "ALIEN"]},
    {"id": "c_loc_archer_iv",    "name": "Archer IV",            "card_type": "LOCATION", "points": 3, "specialty": None,        "traits": []},
    {"id": "c_loc_baku",         "name": "Ba'ku",                "card_type": "LOCATION", "points": 6, "specialty": None,        "traits": ["ANOMALY"]},
    {"id": "c_loc_betazed",      "name": "Betazed",              "card_type": "LOCATION", "points": 3, "specialty": None,        "traits": ["BETAZOID"]},
    {"id": "c_loc_corvan_ii",    "name": "Corvan II",            "card_type": "LOCATION", "points": 3, "specialty": None,        "traits": ["STARFLEET", "BUSINESS", "HUMAN"]},
    {"id": "c_loc_ds_k7",        "name": "Deep Space K-7",       "card_type": "LOCATION", "points": 0, "specialty": "influence", "traits": ["STARBASE"]},
    {"id": "c_loc_delta_vega",   "name": "Delta Vega",           "card_type": "LOCATION", "points": 2, "specialty": None,        "traits": []},
    {"id": "c_loc_derna",        "name": "Derna",                "card_type": "LOCATION", "points": 6, "specialty": None,        "traits": ["BAJORAN", "ROMULAN", "DOCTOR"]},
    {"id": "c_loc_dozaria",      "name": "Dozaria",              "card_type": "LOCATION", "points": 3, "specialty": None,        "traits": ["BREEN"]},
    {"id": "c_loc_freecloud",    "name": "Freecloud",            "card_type": "LOCATION", "points": 5, "specialty": None,        "traits": ["BUSINESS", "SHADY"]},
    {"id": "c_loc_indri_viii",   "name": "Indri VIII",           "card_type": "LOCATION", "points": 5, "specialty": None,        "traits": ["ANOMALY"]},
    {"id": "c_loc_kelvas_docks", "name": "Kelvas Docks",         "card_type": "LOCATION", "points": 0, "specialty": "military",  "traits": ["CARDASSIAN", "STARBASE", "ENGINEER", "DOMINION"]},
    {"id": "c_loc_memory_alpha", "name": "Memory Alpha",         "card_type": "LOCATION", "points": 5, "specialty": None,        "traits": ["COMMUNICATION", "STARFLEET"]},
    {"id": "c_loc_regula_i",     "name": "Regula I",             "card_type": "LOCATION", "points": 6, "specialty": None,        "traits": ["STARFLEET", "SCIENTIST", "STARBASE"]},
    {"id": "c_loc_risa",         "name": "Risa",                 "card_type": "LOCATION", "points": 4, "specialty": None,        "traits": ["BUSINESS"]},
    {"id": "c_loc_solum",        "name": "Solum",                "card_type": "LOCATION", "points": 10,"specialty": None,        "traits": ["ALIEN"]},
    {"id": "c_loc_tulgana_iv",   "name": "Tulgana IV",           "card_type": "LOCATION", "points": 1, "specialty": None,        "traits": ["AMBASSADOR", "STARFLEET", "BUSINESS", "KLINGON"]},
    {"id": "c_loc_verex_iii",    "name": "Verex III",            "card_type": "LOCATION", "points": 5, "specialty": None,        "traits": ["SHADY", "ORION"]},
    {"id": "c_loc_xahea",        "name": "Xahea",                "card_type": "LOCATION", "points": 0, "specialty": "research",  "traits": []},


    # ── SHIP ──────────────────────────────────────────────────────────────────
    {"id": "c_ship_bird_of_prey", "name": "Bird-of-Prey",                "card_type": "SHIP", "points": 2, "specialty": None,        "traits": ["IMPERIAL", "ROMULAN", "ATTACK", "CLOAK"]},
    {"id": "c_ship_borg_probe",   "name": "Borg Probe",                  "card_type": "SHIP", "points": 2, "specialty": None,        "traits": ["BORG"]},
    {"id": "c_ship_dkyr",         "name": "D'Kyr Cruiser",               "card_type": "SHIP", "points": 2, "specialty": None,        "traits": ["SCIENTIST", "VULCAN"]},
    {"id": "c_ship_holo_drone",   "name": "Holographic Drone Ship",      "card_type": "SHIP", "points": 0, "specialty": "influence", "traits": ["HOLOGRAM", "ROMULAN", "WEAPON", "AERNAR"]},
    {"id": "c_ship_ktinga",       "name": "K't'inga Battlecruiser",      "card_type": "SHIP", "points": 0, "specialty": "military",  "traits": ["IMPERIAL", "KLINGON"]},
    {"id": "c_ship_kazon",        "name": "Kazon Raider",                "card_type": "SHIP", "points": 0, "specialty": "influence", "traits": ["ATTACK", "SHADY"]},
    {"id": "c_ship_pakled",       "name": "Pakled Freighter",            "card_type": "SHIP", "points": 2, "specialty": None,        "traits": ["BUSINESS", "PAKLED"]},
    {"id": "c_ship_sona",         "name": "Son'a Battlecruiser",         "card_type": "SHIP", "points": 2, "specialty": None,        "traits": ["DOMINION", "ATTACK", "SHADY"]},
    {"id": "c_ship_ent_c",        "name": "U.S.S. Enterprise-C",         "card_type": "SHIP", "points": 0, "specialty": "research",  "traits": ["TIME TRAVEL", "AMBASSADOR", "STARFLEET"]},
    {"id": "c_ship_pasteur",      "name": "U.S.S. Pasteur",              "card_type": "SHIP", "points": 0, "specialty": "research",  "traits": ["COMMUNICATION", "STARFLEET", "DOCTOR"]},
    {"id": "c_ship_reliant",      "name": "U.S.S. Reliant",              "card_type": "SHIP", "points": 2, "specialty": None,        "traits": ["STARFLEET"]},
    {"id": "c_ship_voth",         "name": "Voth Research Vessel",        "card_type": "SHIP", "points": 2, "specialty": None,        "traits": ["ANOMALY", "ALIEN"]},
    {"id": "c_ship_xindi_rep",    "name": "Xindi-Reptillian Battleship", "card_type": "SHIP", "points": 0, "specialty": "military",  "traits": ["XINDI"]},

    # ── PERSON ────────────────────────────────────────────────────────────────
    {"id": "c_per_jarok",          "name": "Admiral Jarok",      "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["ROMULAN"]},
    {"id": "c_per_nechayev",       "name": "Admiral Nechayev",   "card_type": "PERSON", "points": 0, "specialty": "influence", "traits": ["STARFLEET","HUMAN"]},
    {"id": "c_per_pressman",       "name": "Admiral Pressman",   "card_type": "PERSON", "points": 0, "specialty": "military", "traits": ["STARFLEET", "HUMAN", "SHADY"]},
    {"id": "c_per_kamarag",        "name": "Ambassador Kamarag", "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["AMBASSADOR", "IMPERIAL", "KLINGON"]},
    {"id": "c_per_b4",             "name": "B-4",                "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["SYNTHETIC", "ANDROID", "ATTACK"]},
    {"id": "c_per_maddox",         "name": "Bruce Maddox",       "card_type": "PERSON", "points": 0, "specialty": "research", "traits": ["SCIENTIST", "STARFLEET", "ENGINEER", "HUMAN"]},
    {"id": "c_per_dorg",           "name": "Captain Dorg",       "card_type": "PERSON", "points": 0, "specialty": "military", "traits": ["KLINGON", "ATTACK", "SHADY"]},
    {"id": "c_per_mudd",           "name": "Harry Mudd",         "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["TIME TRAVEL", "ATTACK", "HUMAN", "SHADY"]},
    {"id": "c_per_jorit_dal",      "name": "Jorit Dal",          "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["CARDASSIAN", "STARFLEET", "SPY"]},
    {"id": "c_per_laas",           "name": "Laas",               "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["CHANGELING"]},
    {"id": "c_per_laris",          "name": "Laris",              "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["ROMULAN"]},
    {"id": "c_per_lenara",         "name": "Lenara Kahn",        "card_type": "PERSON", "points": 0, "specialty": "research", "traits": ["SCIENTIST", "TRILL"]},
    {"id": "c_per_lursa",          "name": "Lursa",              "card_type": "PERSON", "points": 0, "specialty": "military", "traits": ["KLINGON", "SHADY"]},
    {"id": "c_per_lwaxana",        "name": "Lwaxana Troi",       "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["AMBASSADOR", "BETAZOID", "TELEPATH"]},
    {"id": "c_per_mirok",          "name": "Mirok",              "card_type": "PERSON", "points": 0, "specialty": "research", "traits": ["SCIENTIST", "ROMULAN", "ATTACK"]},
    {"id": "c_per_moriarty",       "name": "Moriarty",           "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["SYNTHETIC", "HOLOGRAM", "ATTACK", "SHADY"]},
    {"id": "c_per_peanut",         "name": "Peanut Hamper",      "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["SYNTHETIC"]},
    {"id": "c_per_kambarg",        "name": "Phlox",              "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["DOCTOR"]},
    {"id": "c_per_riva",           "name": "Riva",               "card_type": "PERSON", "points": 0, "specialty": "influence", "traits": ["COMMUNICATION", "AMBASSADOR", "TELEPATH"]},
    {"id": "c_per_rom",            "name": "Rom",                "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["ENGINEER", "FERENGI"]},
    {"id": "c_per_sakonna",        "name": "Sakonna",            "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["VULCAN", "MAQUIS"]},
    {"id": "c_per_sukal",          "name": "Su'Kal",             "card_type": "PERSON", "points": 5, "specialty": None, "traits": ["KELPIEN"]},
    {"id": "c_per_talok",          "name": "Talok",              "card_type": "PERSON", "points": 0, "specialty": "influence", "traits": ["ROMULAN", "VULCAN", "ATTACK", "SPY"]},
    {"id": "c_per_tevrin",         "name": "Tevrin Krit",        "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["TELLARITE", "BUSINESS"]},
    {"id": "c_per_zephram",        "name": "Zephram Cochrane",   "card_type": "PERSON", "points": 1, "specialty": None, "traits": ["ENGINEER", "HUMAN", "PILOT"]},

    # ── INCIDENT ──────────────────────────────────────────────────────────────
    {"id": "c_inc_energy_drain",   "name": "Energy Drain",          "card_type": "INCIDENT", "points": -2, "specialty": None, "traits": []},
    {"id": "c_inc_hostile",        "name": "Hostile Contact",       "card_type": "INCIDENT", "points": -2, "specialty": None, "traits": []},
    {"id": "c_inc_political",      "name": "Political Crisis",      "card_type": "INCIDENT", "points": -2, "specialty": None, "traits": []},
    {"id": "c_inc_red_alert",      "name": "Red Alert",             "card_type": "INCIDENT", "points": -2, "specialty": None, "traits": []},
    {"id": "c_inc_subspace",       "name": "Subspace Phenomenon",   "card_type": "INCIDENT", "points": -2, "specialty": None, "traits": []},
    {"id": "c_inc_trade_embargo",  "name": "Trade Embargo",         "card_type": "INCIDENT", "points": -2, "specialty": None, "traits": []},

    # ── ENCOUNTER ─────────────────────────────────────────────────────────────
    {"id": "c_enc_ancient_gene", "name": "Ancient Gene Fragments", "card_type": "ENCOUNTER", "points": 0, "specialty": "military",  "traits": ["ANOMOLY", "AUGMENT"]},
    {"id": "c_enc_boltzmann",    "name": "Boltzmann Brain",        "card_type": "ENCOUNTER", "points": 6, "specialty": None,        "traits": ["TELEPATH", "DOCTOR"]},
    {"id": "c_enc_guardian",     "name": "Guardian of Forever",    "card_type": "ENCOUNTER", "points": 3, "specialty": None,        "traits": ["TRANSCENDENT", "TIME TRAVEL", "ONGOING", "ANOMOLY"]},
    {"id": "c_enc_iconian",      "name": "Iconian Gateway",        "card_type": "ENCOUNTER", "points": 0, "specialty": "influence", "traits": ["IMPERIAL", "ALIEN"]},
    {"id": "c_enc_koala",        "name": "Koala",                  "card_type": "ENCOUNTER", "points": 8, "specialty": None,        "traits": ["WILDCARD"]},
    {"id": "c_enc_omega",        "name": "Omega Particle",         "card_type": "ENCOUNTER", "points": 0, "specialty": "research",  "traits": ["SCIENTIST"]},
    {"id": "c_enc_ova_ka_ree",   "name": "Sha Ka Ree",             "card_type": "ENCOUNTER", "points": 7, "specialty": None,        "traits": ["TRANSCENDENT", "ONGOING", "ATTACK", "VULCAN"]},
    {"id": "c_enc_vger",         "name": "V'Ger",                  "card_type": "ENCOUNTER", "points": 9, "specialty": None,        "traits": ["SYNTHETIC"]},
]

# Index for fast lookup
BY_ID = {c["id"]: c for c in CARDS}

# Group by card_type for the "gain card" selector
BY_TYPE: dict[str, list] = {}
for _c in CARDS:
    BY_TYPE.setdefault(_c["card_type"], []).append(_c)
