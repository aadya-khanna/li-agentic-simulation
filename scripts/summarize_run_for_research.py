#!/usr/bin/env python3
"""Generate a research/runs note from a completed experiment directory."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.config import Settings  # noqa: E402
from li_sim.research_log import write_research_note  # noqa: E402
from li_sim.runs import resolve_run_dir  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Write research/runs note from experiment tape")
    parser.add_argument(
        "run_dir",
        nargs="?",
        type=Path,
        default=None,
        help="Run dir under logs/ (default: latest)",
    )
    parser.add_argument("--stub", action="store_true", help="Use stub summarizer (no API)")
    parser.add_argument("--run-number", type=int, default=None, help="Override run number (tests)")
    args = parser.parse_args()

    run_dir = resolve_run_dir(args.run_dir)
    settings = Settings(stub=args.stub)
    out = write_research_note(run_dir, settings, number=args.run_number)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
