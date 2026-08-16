#!/usr/bin/env python3
"""Build a short drama headline log from an experiment events tape."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.brief import (  # noqa: E402
    load_events_from_path,
    print_brief_panel,
    summarize_events,
    write_brief_log,
)
from li_sim.runs import resolve_run_dir  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize main villa drama from events.jsonl")
    parser.add_argument(
        "run_dir",
        nargs="?",
        type=Path,
        default=None,
        help="Run directory under logs/ (default: latest run)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Write brief log here (default: brief.log in run dir)",
    )
    parser.add_argument("--print", action="store_true", help="Also print to terminal")
    args = parser.parse_args()

    base = resolve_run_dir(args.run_dir)
    events_path = base / "events.jsonl"
    events = load_events_from_path(events_path)
    if not events:
        raise SystemExit(f"No events in {events_path}")

    brief = summarize_events(events)
    out = args.output or base / "brief.log"
    write_brief_log(brief, out)
    print(f"Wrote {len(brief)} headline(s) to {out}")
    if args.print:
        print_brief_panel(brief)


if __name__ == "__main__":
    main()
