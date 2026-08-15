# Tool: run season

## Stub (default for dev)

```bash
python scripts/run_villa.py --stub --days 1
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

| File | Contents |
|------|----------|
| `logs/run.jsonl` | One JSON event per line |
| `logs/thoughts.jsonl` | Private thought events only |
| `logs/run-state.json` | Final villa checkpoint |

Each run **overwrites** these files.
