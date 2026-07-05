from dataclasses import dataclass

@dataclass
class Ruleset:
    salary_cap: int
    slot_requirements: dict
   

RULESETS = {
    ("DraftKings", "classic", "MLB"): 
        Ruleset(
            salary_cap=50000,
            slot_requirements = {
                "P": 2,
                "C": 1,
                "1B": 1,
                "2B": 1,
                "3B": 1,
                "SS": 1,
                "OF": 3,
            },
        ),
    ("Fanduel", "classic", "MLB"): 
        Ruleset(
            salary_cap=35000,
            slot_requirements = {
                "P": 1,
                "C/1B": 1,
                "2B": 1,
                "3B": 1,
                "SS": 1,
                "OF": 3,
                "UTIL": 1,
            },
        ),
        ("DraftKings", "classic", "NFL"):
            Ruleset(
                salary_cap=50000,
                slot_requirements = {
                    "QB": 1,
                    "RB": 2,
                    "WR": 3,
                    "TE": 1,
                    "FLEX": 1,
                    "DST": 1,
                },
            ),
        ("Fanduel", "classic", "NFL"):
            Ruleset(
                salary_cap=60000,
                slot_requirements = {
                    "QB": 1,
                    "RB": 2,
                    "WR": 3,
                    "TE": 1,
                    "FLEX": 1,
                    "D": 1,
                },
            ),
        ("DraftKings", "classic", "NBA"):
            Ruleset(
                salary_cap=50000,
                slot_requirements = {
                    "PG": 1,
                    "SG": 1,
                    "SF": 1,
                    "PF": 1,
                    "C": 1,
                    "G": 1,
                    "F": 1,
                    "UTIL": 1,
                },
            ),
        ("Fanduel", "classic", "NBA"):
            Ruleset(
                salary_cap=60000,
                slot_requirements = {
                    "PG": 2,
                    "SG": 2,
                    "SF": 2,
                    "PF": 2,
                    "C": 1,
                },
            ),
        ("DraftKings", "classic", "NHL"):
            Ruleset(
                salary_cap=50000,
                slot_requirements = {
                    "C": 2,
                    "W": 3,
                    "D": 2,
                    "FLEX": 1,
                    "G": 1,
                },
            ),
        ("Fanduel", "classic", "NHL"):
            Ruleset(
                salary_cap=55000,
                slot_requirements = {
                    "C": 2,
                    "W": 2,
                    "D": 2,
                    "UTIL": 2,
                    "G": 1,
                },
            ),
        ("DraftKings", "classic", "CFB"):
            Ruleset(
                salary_cap=50000,
                slot_requirements = {
                    "QB": 2,
                    "RB": 2,
                    "WR": 3,
                    "TE": 1,
                    "FLEX": 1,
                },
            ),
        # Check lineup requirements when CFB goes live to confirm correct Ruleset
        ("Fanduel", "classic", "CFB"):
            Ruleset(
                salary_cap=60000,
                slot_requirements = {
                    "QB": 1,
                    "RB": 2,
                    "WR/TE": 3,
                    "Super FLEX": 1,
                },
            ),
        ("DraftKings", "classic", "PGA"):
            Ruleset(
                salary_cap=50000,
                slot_requirements = {
                    "GOLFER": 6,
                },
            ),
        ("Fanduel", "classic", "PGA"):
            Ruleset(
                salary_cap=60000,
                slot_requirements = {
                    "GOLFER": 6,
                },
            ),
    }
