# scripts/test_dk_import.py
from app.db import engine
from app.ingestion.dk_csv_importer import import_dk_csv
from sqlmodel import Session

with Session(engine) as session:
    import_dk_csv(session, "data/mlb_slate.csv", sport="MLB")

print("Import complete.")