from fastapi import FastAPI
from .agents.research_agent.agent import build

app = FastAPI()
_agent = build()


@app.get("/healthz")
def healthz():
    return {"ok": True, "agent": "research_agent"}


@app.post("/ping")
def ping(payload: dict):
    return _agent.handle("ping", payload)
