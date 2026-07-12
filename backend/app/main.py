from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from app.optimizer.solver import build_lineup


app = FastAPI(title="DFS Optimizer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/lineup")
def get_lineup(
    sport: str = "MLB", 
    site: str = "DraftKings", 
    salary_cap: int | None = None,
    session: Session = Depends(get_session),
):
    try:
        result = build_lineup(session, sport=sport, site=site, salary_cap=salary_cap)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if result is None:
        raise HTTPException(
            status_code=422,
            detail=f"No feasible lineup for site='{site}', sport='{sport}' with current data/salary cap."
        )
    return {"lineup": result}