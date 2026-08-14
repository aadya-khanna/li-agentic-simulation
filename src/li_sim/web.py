from __future__ import annotations

import json

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .config import LOG_DIR, ROOT
from .logging_utils import load_events

STATIC_DIR = ROOT / "viewer" / "static"


def create_app() -> FastAPI:
    app = FastAPI(title="Love Island Simulation Viewer")

    @app.get("/api/thoughts")
    def api_thoughts():
        return load_events(LOG_DIR / "thoughts.jsonl")

    @app.get("/api/state")
    def api_state():
        path = LOG_DIR / "run-state.json"
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))

    @app.get("/")
    def index():
        return FileResponse(STATIC_DIR / "index.html")

    if STATIC_DIR.exists():
        app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    return app


app = create_app()


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8765, reload=False)
