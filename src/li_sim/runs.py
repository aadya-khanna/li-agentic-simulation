from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from .config import LOG_DIR, Settings

LATEST_POINTER = LOG_DIR / "latest.json"


def default_run_id() -> str:
    return datetime.now(UTC).strftime("%Y%m%d-%H%M%S")


def write_latest_pointer(run_dir: Path) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    rel = run_dir.relative_to(LOG_DIR)
    LATEST_POINTER.write_text(json.dumps({"run_dir": rel.as_posix()}, indent=2) + "\n", encoding="utf-8")


def resolve_run_dir(explicit: Path | None = None) -> Path:
    if explicit is not None:
        path = explicit if explicit.is_absolute() else LOG_DIR / explicit
        if not path.exists():
            raise FileNotFoundError(f"run directory not found: {path}")
        return path
    if LATEST_POINTER.exists():
        data = json.loads(LATEST_POINTER.read_text(encoding="utf-8"))
        return LOG_DIR / data["run_dir"]
    experiments = LOG_DIR / "experiments"
    if not experiments.exists():
        raise FileNotFoundError("no experiment runs found under logs/experiments/")
    manifests = list(experiments.rglob("manifest.json"))
    if not manifests:
        raise FileNotFoundError("no manifest.json files found under logs/experiments/")
    latest = max(manifests, key=lambda path: path.stat().st_mtime)
    return latest.parent


def events_path_for(settings: Settings) -> Path:
    return settings.run_dir() / "events.jsonl"
