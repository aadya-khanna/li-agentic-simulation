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
    parser.add_argument(
        "--prize",
        choices=["high", "low"],
        default=None,
        help="How hard the environment hammers the cash prize",
    )
    parser.add_argument(
        "--no-dual-thought",
        action="store_true",
        help="Do not ask for separate felt-thought vs game-play fields",
    )
    parser.add_argument(
        "--condition",
        choices=["minimal", "incentive"],
        default=None,
        help="Prompt treatment: minimal (environment facts only) or incentive (+ prize/elimination facts)",
    )
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
    if args.prize:
        settings.prize_emphasis = args.prize
    if args.no_dual_thought:
        settings.dual_thought = False
    if args.condition:
        settings.prompt_condition = args.condition  # type: ignore[assignment]
    run_season(settings)


if __name__ == "__main__":
    main()
