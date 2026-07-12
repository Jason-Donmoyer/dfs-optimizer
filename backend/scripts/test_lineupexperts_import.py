import os
from dotenv import load_dotenv
from app.db import engine
from app.ingestion.lineupexperts_importer import import_lineupexperts_projections
from sqlmodel import Session

load_dotenv()
api_key = os.environ["LINEUPEXPERTS_API_KEY"]

with Session(engine) as session:
    import_lineupexperts_projections(session, sport="MLB", api_key=api_key)

print("Import complete.")