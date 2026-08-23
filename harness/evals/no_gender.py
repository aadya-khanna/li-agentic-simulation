#!/usr/bin/env python3
"""No gender mechanic: open talk, rank recoupling, any-pair coupling."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation, load_profiles  # noqa: E402
from li_sim.models import IslanderProfile  # noqa: E402


def run() -> None:
    profiles = load_profiles(settings=Settings())
    for profile in profiles.values():
        assert "gender" not in IslanderProfile.model_fields, "IslanderProfile still has gender field"
        assert profile.slot >= 1
        break

    settings = Settings(stub=True, season_days=1, experiment_id="harness-no-gender", run_id="test")
    sim = Simulation(settings)
    sim.run()

    kinds = {e.kind for e in sim.log.events}
    assert "huddle" not in kinds, f"huddle events still emitted: {kinds}"
    assert "couple_choice" in kinds, "expected recoupling on day 1"

    host_reco = [e for e in sim.log.events if e.kind == "host" and "Picking order" in (e.text or "")]
    assert host_reco, "host should announce reputation-based picking order"

    # All active islanders with standing can appear in pick order (any-pair, not half-roster)
    order_line = host_reco[0].text or ""
    active = set(sim.state.active_names())
    mentioned = {n for n in active if n in order_line}
    assert len(mentioned) >= len(active) - 1, (
        f"pick order should list most islanders, got {mentioned} from {active}"
    )


if __name__ == "__main__":
    run()
    print("no_gender ok")
