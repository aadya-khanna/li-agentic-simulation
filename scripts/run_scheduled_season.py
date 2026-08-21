#!/usr/bin/env python3
"""Run a scheduled 7-day live season (cron / GitHub Actions entrypoint)."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "harness"))

from analysis.metrics import write_metrics  # noqa: E402
from li_sim.brief import summarize_events, write_brief_log  # noqa: E402
from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation  # noqa: E402
from li_sim.research_log import write_research_note  # noqa: E402

EXPERIMENT_ID = "scheduled"


def condition_for_utc_hour(hour: int | None = None) -> str:
    """Rotate minimal (0 UTC) and incentive (12 UTC) for 12-hour cron slots."""
    hour = datetime.now(UTC).hour if hour is None else hour
    return "incentive" if hour == 12 else "minimal"


def cron_run_id(when: datetime | None = None) -> str:
    when = when or datetime.now(UTC)
    return f"cron-{when.strftime('%Y%m%d-%H%M')}"


def seed_from_timestamp(when: datetime | None = None) -> int:
    when = when or datetime.now(UTC)
    return int(when.strftime("%Y%m%d%H"))


def run_scheduled(
    *,
    live: bool = True,
    condition: str | None = None,
    seed: int | None = None,
    run_id: str | None = None,
    write_research: bool = True,
    stub_summarizer: bool = False,
) -> Path:
    now = datetime.now(UTC)
    condition = condition or condition_for_utc_hour(now.hour)
    seed = seed if seed is not None else seed_from_timestamp(now)
    run_id = run_id or cron_run_id(now)

    settings = Settings(
        stub=not live,
        season_days=7,
        prompt_condition=condition,  # type: ignore[arg-type]
        seed=seed,
        experiment_id=EXPERIMENT_ID,
        run_id=run_id,
    )
    print(
        json.dumps(
            {
                "experiment_id": EXPERIMENT_ID,
                "condition": condition,
                "run_id": run_id,
                "seed": seed,
                "live": live,
            },
            indent=2,
        ),
        flush=True,
    )
    sim = Simulation(settings)
    sim.run()
    run_dir = settings.run_dir()
    write_metrics(settings.events_path)
    brief = summarize_events(sim.log.events)
    write_brief_log(brief, run_dir / "brief.log")
    if write_research:
        summary_settings = Settings(stub=stub_summarizer or not live)
        note = write_research_note(run_dir, summary_settings)
        print(f"research note: {note}", flush=True)
    print(f"run_dir: {run_dir}", flush=True)
    return run_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Scheduled 7-day season for cron/GHA")
    parser.add_argument("--live", action="store_true", help="Use live LLM (default for cron)")
    parser.add_argument("--stub", action="store_true", help="Stub season (local dry-run)")
    parser.add_argument("--condition", choices=["minimal", "incentive"], default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--run-id", type=str, default=None)
    parser.add_argument(
        "--no-research-note",
        action="store_true",
        help="Skip research/runs note generation",
    )
    parser.add_argument(
        "--stub-summarizer",
        action="store_true",
        help="Write research note with stub summarizer (no analyst LLM call)",
    )
    args = parser.parse_args()
    live = args.live and not args.stub
    run_scheduled(
        live=live,
        condition=args.condition,
        seed=args.seed,
        run_id=args.run_id,
        write_research=not args.no_research_note,
        stub_summarizer=args.stub_summarizer or args.stub,
    )


if __name__ == "__main__":
    main()
