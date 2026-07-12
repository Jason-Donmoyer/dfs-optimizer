from app.db import engine
from app.models import ProjectionSource
from sqlmodel import Session

sources = [
    ProjectionSource(name="DraftKings FPPG", default_weight=0.2),
    ProjectionSource(name="LineupExperts", default_weight=0.5),
    # ProjectionSource(name="FreeSource", default_weight=0.3),
]

with Session(engine) as session:
    for source in sources:
        session.add(source)
    session.commit()

print("Seeded projection sources.")