# Tool: run season

## Stub (default for dev)

```bash
python scripts/run_villa.py --stub --days 1
python scripts/run_villa.py --stub --days 7 --condition minimal --seed 42
python scripts/run_villa.py --stub --days 2 --prize low
python scripts/run_villa.py --stub --no-dual-thought --days 1
```

## Live

Requires `.env` with `LI_STUB=0` and a provider key.

```bash
python scripts/run_villa.py --live --days 3 --prize high
python scripts/run_villa.py --live --model gpt-4o-mini --rpm 8
```

## Outputs

Each run writes an isolated directory:

```
logs/experiments/<experiment_id>/<condition>/<run_id>/
  events.jsonl
  decisions.jsonl
  thoughts.jsonl
  state.json
  manifest.json
  brief.log
```

Default: `experiment_id=local`, `run_id=<timestamp>`. `logs/latest.json` points at the most recent run.

Named experiment:

```bash
python scripts/run_villa.py --stub --days 1 \
  --experiment-id my-study --run-id seed-1 --condition minimal
```
