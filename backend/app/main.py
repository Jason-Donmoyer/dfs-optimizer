from fastapi import FastAPI

app = FastAPI(title="DFS Optimizer")

@app.get("/health")
def health():
    return {"status": "ok"}