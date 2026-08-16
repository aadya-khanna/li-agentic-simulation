from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .config import LOG_DIR, ROOT
from .logging_utils import load_events
from .runs import resolve_run_dir

STATIC_DIR = ROOT / "viewer" / "static"


def create_app(run_dir: Path | None = None) -> FastAPI:
    app = FastAPI(title="Love Island Simulation Viewer")
    base = resolve_run_dir(run_dir)

    @app.get("/api/run")
    def api_run():
        manifest = base / "manifest.json"
        if manifest.exists():
            return json.loads(manifest.read_text(encoding="utf-8"))
        return {"run_dir": str(base.relative_to(LOG_DIR))}

    @app.get("/api/events")
    def api_events():
        return load_events(base / "events.jsonl")

    @app.get("/api/thoughts")
    def api_thoughts():
        return load_events(base / "thoughts.jsonl")

    @app.get("/api/state")
    def api_state():
        path = base / "state.json"
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
    import argparse
    import uvicorn

    parser = argparse.ArgumentParser(description="Replay the latest experiment run")
    parser.add_argument(
        "--run-dir",
        type=str,
        default=None,
        help="Path to a run directory under logs/ (default: latest run)",
    )
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    run_path = Path(args.run_dir) if args.run_dir else None
    uvicorn.run(create_app(run_path), host="127.0.0.1", port=args.port, reload=False)
