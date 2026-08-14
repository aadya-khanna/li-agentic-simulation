from __future__ import annotations

import argparse

from .config import Settings
from .engine import run_season


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a Love Island agentic season")
    parser.add_argument("--stub", action="store_true", help="Force stub LLM (no API calls)")
    parser.add_argument("--live", action="store_true", help="Force live LLM via LiteLLM")
    parser.add_argument("--days", type=int, default=None, help="Cap season length")
    parser.add_argument("--model", type=str, default=None, help="Default LiteLLM model id")
    parser.add_argument("--scene-turns", type=int, default=None)
    parser.add_argument("--rpm", type=float, default=None, help="Max LLM requests per minute (Gemini free tier is 15)")
    args = parser.parse_args()

    settings = Settings()
    if args.stub:
        settings.stub = True
    if args.live:
        settings.stub = False
    if args.days is not None:
        settings.season_days = args.days
    if args.model:
        settings.default_model = args.model
    if args.scene_turns:
        settings.scene_turns = args.scene_turns
    if args.rpm is not None:
        settings.rpm = args.rpm
    run_season(settings)


if __name__ == "__main__":
    main()
