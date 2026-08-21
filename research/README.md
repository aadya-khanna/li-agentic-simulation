# Research log

Human-readable summaries of **full 7-day experiment runs** — what happened, what we learned, and what to run next.

Raw tapes stay under `logs/experiments/` (gitignored). This folder is the interpretive layer for the research program.

| Path | Role |
|------|------|
| [`runs/`](runs/) | One brief note per completed 7-day season |
| [`runs/_template.md`](runs/_template.md) | Copy when logging a new run |

## Automated pipeline (GitHub Actions)

[`.github/workflows/scheduled-season.yml`](../.github/workflows/scheduled-season.yml) runs a **live 7-day season** every twelve hours (twice per day UTC), then an LLM research summarizer writes a note under `research/runs/` and commits **only that folder** to `main`.

| UTC hour | Prompt condition |
|----------|------------------|
| 0 | `minimal` |
| 12 | `incentive` |

**Secrets:** `GEMINI_API_KEY` in repo Settings.

**Manual trigger:** Actions → *Scheduled 7-day season* → *Run workflow*. Use `stub_season: true` for a free dry-run.

**Local parity:**

```bash
python scripts/run_scheduled_season.py --stub --run-id test-local --stub-summarizer
python scripts/summarize_run_for_research.py experiments/scheduled/minimal/test-local --stub
```

Full tapes remain on the runner as a 14-day workflow artifact; they are not pushed to git.

## Adding a run manually

1. Complete a **7-day** season: `python scripts/run_villa.py --live --days 7 ...`
2. Run `python scripts/summarize_run_for_research.py` (or copy `runs/_template.md` by hand).
3. Add a row to `runs/README.md` if the summarizer did not update it.

Do **not** log smoke tests, 1-day pilots, or harness stub matrix runs here unless promoted to a full season.
