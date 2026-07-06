from app.models.player import SlateProjection, ProjectionSource
from sqlmodel import select

def get_blended_projection(session, player_slate_id: int) -> float:
    statement = (
        select(SlateProjection, ProjectionSource)
        .join(ProjectionSource, SlateProjection.source_id == ProjectionSource.id)
        .where(SlateProjection.player_slate_id == player_slate_id)
    )
    rows = session.exec(statement).all()

    weighted_total = 0
    weight_total = 0

    for slate_projection, source in rows:
        weighted_total += slate_projection.projection * source.default_weight
        weight_total += source.default_weight
    
    if weight_total == 0:
        return None
    
    return weighted_total / weight_total

    

