COMPOUND_SLOT_MAP = {
    ("DraftKings", "NFL"): {"FLEX": ["RB", "WR", "TE"]},
    ("DraftKings", "CFB"): {"FLEX": ["RB", "WR", "TE"]},
    ("DraftKings", "NBA"): {"G": ["PG", "SG"], "F": ["SF", "PF"], "UTIL": ["PG", "SG", "SF", "PF", "C"]},
    ("DraftKings", "NHL"): {"FLEX": ["C", "W", "D"]},
    ("Fanduel", "NFL"): {"FLEX": ["RB", "WR", "TE"]},
    ("Fanduel", "CFB"): {"WR/TE": ["WR", "TE"], "Super FLEX": ["QB", "RB", "WR", "TE"]},
    ("Fanduel", "NHL"): {"UTIL": ["C", "W", "D"]},
    ("Fanduel", "MLB"): {"C/1B": ["C", "1B"], "UTIL": ["C", "1B", "2B", "3B", "SS", "OF"]},
}

def get_extra_slots(site: str, sport: str, real_position: str) -> list[str]:
    """
    Given a player's real position, return any additional compound slots
    (beyond their natural position) they're eligible for on this site/sport.
    """
    compound_slots_for_this_context = COMPOUND_SLOT_MAP.get((site, sport), {})

    extra_slots = []
        
    for slot_name, eligible_positions in compound_slots_for_this_context.items():
        if real_position in eligible_positions:
            extra_slots.append(slot_name)

    return extra_slots