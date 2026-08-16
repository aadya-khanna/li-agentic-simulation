#!/usr/bin/env python3
"""Build a short drama headline log from a run.jsonl tape."""
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize main villa drama from run.jsonl")
    parser.add_argument(
        "log",
        nargs="?",
        type=Path,
        default=ROOT / "logs" / "run.jsonl",
        help="Path to run.jsonl (default: logs/run.jsonl)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Write brief log here (default: brief.log next to input)",
    )
    parser.add_argument("--print", action="store_true", help="Also print to terminal")
    args = parser.parse_args()

    events = load_events_from_path(args.log)
    if not events:
        raise SystemExit(f"No events in {args.log}")

    brief = summarize_events(events)
    out = args.output or args.log.parent / "brief.log"
    write_brief_log(brief, out)
    print(f"Wrote {len(brief)} headline(s) to {out}")
    if args.print:
        print_brief_panel(brief)


if __name__ == "__main__":
    main()
