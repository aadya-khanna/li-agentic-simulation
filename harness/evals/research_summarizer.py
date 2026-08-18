#!/usr/bin/env python3
"""Research summarizer produces template-shaped stub output from fixture tape."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.config import Settings  # noqa: E402
from li_sim.research_log import (  # noqa: E402
    build_event_excerpt,
    generate_summary_text,
    load_run_context,
    load_run_events,
    slug_for_run,
)


def run() -> None:
    fixture = ROOT / "harness" / "fixtures" / "research-run"
    context = load_run_context(fixture)
    assert context["event_count"] >= 5, "fixture events too sparse"
    excerpt = context["excerpt"]
    assert "pick:" in excerpt or "dump:" in excerpt, f"excerpt missing ceremony lines: {excerpt!r}"
    assert "Top talk pairs:" in build_event_excerpt(load_run_events(fixture))

    summary = generate_summary_text(context, Settings(stub=True))
    for key in ("headline_arc", "insights", "limits", "next_steps"):
        assert summary[key].strip(), f"empty {key} in stub summary"

    slug = slug_for_run(context["manifest"])
    assert slug.startswith("scheduled-minimal"), slug
    assert "cron-fixture" in slug


if __name__ == "__main__":
    run()
    print("research_summarizer ok")
