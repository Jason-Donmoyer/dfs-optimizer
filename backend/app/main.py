from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from app.optimizer.solver import build_lineup


app = FastAPI(title="DFS Optimizer")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/lineup")
def get_lineup(sport: str = "MLB", site: str = "DraftKings", session: Session = Depends(get_session)):
    result = build_lineup(session, sport=sport, site=site)
    if result is None:
        raise HTTPException(
            status_code=400,
            detail=f"No ruleset found for site='{site}', sport='{sport}'. Check spelling/casing."
        )
    return {"lineup": result}