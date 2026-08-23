#!/usr/bin/env python3
"""Run all harness evals. Exit non-zero on failure."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parent


def _load(name: str):
    path = EVALS_DIR / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load eval: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    failed = 0
    for name in ("prompt_invariants", "smoke_season", "brief_log", "reproducibility", "seed_variation", "decision_trace", "research_summarizer", "belief_memory", "no_gender", "neutral_handles", "hidden_standing", "earned_events", "fallback_hardening"):
        print(f"-- eval: {name} --")
        mod = _load(name)
        try:
            mod.run()
            print(f"   ok: {name}")
        except AssertionError as exc:
            print(f"   FAIL: {name}: {exc}", file=sys.stderr)
            failed += 1
        except Exception as exc:
            print(f"   ERROR: {name}: {exc}", file=sys.stderr)
            failed += 1
    if failed:
        print(f"\n{failed} eval(s) failed", file=sys.stderr)
        return 1
    print("\nall evals passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
