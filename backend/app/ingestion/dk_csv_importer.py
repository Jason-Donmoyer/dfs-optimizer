# app/ingestion/dk_csv_importer.py

import csv
from sqlmodel import Session, select
from app.db import engine
from app.models import Player, PlayerSlate, PlayerSlotEligibility, ProjectionSource, SlateProjection, Sport, ContestType
from app.optimizer.compound_slots import get_extra_slots


def import_dk_csv(session, filepath: str, sport: str, site: str = "DraftKings"):
    # Look up the DK FPPG source once, outside the loop (not per-row)
    dk_source = session.exec(
        select(ProjectionSource).where(ProjectionSource.name == "DraftKings FPPG")
    ).first()

    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            player = Player(
                name=row["Name"],
                sport=Sport(sport),
                team=row["TeamAbbrev"],
                real_position=row["Position"],
            )
            slate = PlayerSlate(
                player=player,
                site=site,
                contest_type=ContestType.CLASSIC,
                salary=int(row["Salary"]),
                projection=0.0,  # placeholder - real value comes from SlateProjection below
            )
            slot_positions = row["Roster Position"].split("/")
            for slot in slot_positions:
                slot_eligibility = PlayerSlotEligibility(
                    slot=slot,
                    player_slate=slate,
                )
            extra_slots = get_extra_slots(site, sport, row["Position"])
            for slot in extra_slots:
                slot_eligibility = PlayerSlotEligibility(
                    slot=slot,
                    player_slate=slate,
                )
            slate_projection = SlateProjection(
                player_slate=slate,
                source=dk_source,
                projection=float(row["AvgPointsPerGame"]),
            )

            session.add(player)

    session.commit()