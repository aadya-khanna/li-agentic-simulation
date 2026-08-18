# Research log

Human-readable summaries of **full 7-day experiment runs** — what happened, what we learned, and what to run next.

Raw tapes stay under `logs/experiments/` (gitignored). This folder is the interpretive layer for the research program.

| Path | Role |
|------|------|
| [`runs/`](runs/) | One brief note per completed 7-day season |
| [`runs/_template.md`](runs/_template.md) | Copy when logging a new run |

## Adding a run

1. Complete a **7-day** season: `python scripts/run_villa.py --live --days 7 ...`
2. Copy `runs/_template.md` → `runs/NNN-<short-slug>.md`.
3. Fill in config, headline arc, insights, limits, and next steps.
4. Add a row to `runs/README.md`.

Do **not** log smoke tests, 1-day pilots, or harness stub matrix runs here unless promoted to a full season.
