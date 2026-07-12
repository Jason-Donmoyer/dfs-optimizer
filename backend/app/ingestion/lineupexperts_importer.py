import requests
from sqlmodel import Session, select
from app.db import engine
from app.models import Player, PlayerSlate, ProjectionSource, SlateProjection

def import_lineupexperts_projections(session, sport: str, api_key: str, site: str = "DraftKings"):
    source = session.exec(
        select(ProjectionSource).where(ProjectionSource.name == "LineupExperts")
    ).first()

    url = f"https://api.lineupexperts.com/v1/{sport.lower()}-ProjectionsInSeason"
    response = requests.get(url, params={"key": api_key, "interval": "today"})
    data = response.json()

    for player_id, entry in data.items():
        name = entry["Player"]["PlayerName"]
        fpts = entry["ProjectedStats"]["FPTS"]

        player = session.exec(
            select(Player).where(Player.name == name)
        ).first()

        if player is None:
            continue

        existing_slate = session.exec(
            select(PlayerSlate).where(
                PlayerSlate.player_id == player.id,
                PlayerSlate.site == site
            )
        ).first()

        if existing_slate is None:
            continue

        slate_projection = SlateProjection(
            player_slate=existing_slate,
            source=source,
            projection=float(fpts)
        )

        session.add(slate_projection)

    session.commit()