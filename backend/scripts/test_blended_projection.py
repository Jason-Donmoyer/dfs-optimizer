from app.db import engine
from app.models import PlayerSlate, ProjectionSource, SlateProjection, Player, Sport, ContestType
from app.optimizer.projections import get_blended_projection
from sqlmodel import Session
from sqlmodel import select

with Session(engine) as session:
    # grab any existing player_slate to test against
    slate = session.exec(select(PlayerSlate)).first()
    sources = session.exec(select(ProjectionSource)).all()

    # add one fake SlateProjection per source, pointing at that slate
    test_values = [15.0, 20.0, 18.0]
    for source, value in zip(sources, test_values):
        session.add(SlateProjection(player_slate_id=slate.id, source_id=source.id, projection=value))
    session.commit()

    result = get_blended_projection(session, slate.id)
    print("Blended projection:", result)