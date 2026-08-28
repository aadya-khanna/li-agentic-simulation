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
        "--stub-on-error",
        action="store_true",
        help="Fall back to stub decisions after LLM retries fail (keeps long live seasons alive)",
    )
    parser.add_argument(
        "--prize",
        choices=["high", "low"],
        default=None,
        help="How hard the environment hammers the cash prize",
    )
    parser.add_argument(
        "--condition",
        choices=["minimal", "incentive"],
        default=None,
        help="Prompt treatment: minimal (environment facts only) or incentive (+ prize/elimination facts)",
    )
    parser.add_argument("--seed", type=int, default=None, help="Deterministic engine seed")
    parser.add_argument("--experiment-id", type=str, default=None, help="Experiment folder name")
    parser.add_argument("--run-id", type=str, default=None, help="Run folder name within experiment")
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
    if args.stub_on_error:
        settings.stub_on_error = True
    if args.prize:
        settings.prize_emphasis = args.prize
    if args.condition:
        settings.prompt_condition = args.condition  # type: ignore[assignment]
    if args.seed is not None:
        settings.seed = args.seed
    if args.experiment_id:
        settings.experiment_id = args.experiment_id
    if args.run_id:
        settings.run_id = args.run_id
    run_season(settings)


if __name__ == "__main__":
    main()
