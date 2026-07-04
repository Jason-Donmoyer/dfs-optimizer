from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpBinary, LpStatus

from sqlmodel import Session, select
from app.db import engine
from app.models import Player, PlayerSlate, PlayerSlotEligibility

# Salary cap variable - will change dynamically based on contest
salary_cap = 60000

# Slot requirements - will change dynamically based on contest
slot_requirements = {
    "QB": 1,
    "RB": 2,
    "WR": 3,
    "TE": 1,
    "FLEX": 1,
    "DST": 1,
}

def main():
    with Session(engine) as session:
        statement = (
            select(Player, PlayerSlate, PlayerSlotEligibility)
            .join(PlayerSlate, PlayerSlate.player_id == Player.id)
            .join(PlayerSlotEligibility, PlayerSlotEligibility.player_slate_id ==PlayerSlate.id)
        )
        rows = session.exec(statement).all()

        # Problem
        prob = LpProblem("DFS_Lineup", LpMaximize)

        # Variables
        x = {
            (player.id, eligibility.slot): LpVariable(f"{player.name}_{player.id}_{eligibility.slot}", cat=LpBinary)
            for player, slate, eligibility in rows
        }

        # Objective
        prob += lpSum(x[(player.id, eligibility.slot)] * slate.projection for player, slate, eligibility in rows)

        # CONSTRAINTS

        # Salary Cap
        prob += lpSum(x[(player.id, eligibility.slot)] * slate.salary for player, slate, eligibility in rows) <= salary_cap
        # One slot per player
        player_ids = {player.id for player, slate, eligibility in rows}

        for player_id in player_ids:
            this_players_rows = [
                (player, slate, eligibility)
                for player, slate, eligibility in rows
                if player.id == player_id
            ]
            prob += lpSum(x[(player.id, eligibility.slot)] for player, slate, eligibility in this_players_rows) <= 1
        # Position constraint based on contest
        for slot in slot_requirements:
            this_slots_rows = [
                (player, slate, eligibility)
                for player, slate, eligibility in rows
                if eligibility.slot.value == slot
            ]
            prob += lpSum(x[(player.id, eligibility.slot)] for player, slate, eligibility in this_slots_rows) == slot_requirements[slot]

        prob.solve()
        print("Status:", LpStatus[prob.status])

        if LpStatus[prob.status] != "Optimal":
            print("No valid lineup found - check constraints/data")
        else:
            total_salary = 0
            for player, slate, eligibility in rows:
                if x[(player.id, eligibility.slot)].value() == 1:
                    print(f"Selected: {player.name} - {eligibility.slot.value} - {slate.salary}")
                    total_salary += slate.salary
        print(f"\nTotal salary: ${total_salary} / ${salary_cap}")

if __name__ == "__main__":
    main()