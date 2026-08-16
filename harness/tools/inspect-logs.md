# Tool: inspect logs

## Viewer (recommended)

```bash
python viewer/app.py
# http://127.0.0.1:8765 — reads logs/latest.json

python viewer/app.py --run-dir experiments/baseline-v1/minimal/seed-1
```

Toggle private thoughts, game-play, whispers, diary.

## CLI snippets

```bash
# Latest run path
cat logs/latest.json

# Event count
wc -l logs/experiments/local/minimal/*/events.jsonl

# Last 5 events (pretty)
RUN=$(python -c "import json; print(json.load(open('logs/latest.json'))['run_dir'])")
tail -5 logs/$RUN/events.jsonl | python -m json.tool

# All recoupling picks
grep couple_choice logs/$RUN/events.jsonl | python -m json.tool

# Brief drama headline log
python scripts/brief_log.py --print
```

## Checkpoint fields

`state.json` in each run directory includes `islanders.<name>.contacts` (talk counts), `coupled_with`, `memories`, `inner_thoughts`.

## Analysis prompts

When comparing runs, diff:

1. Recoupling `text` + paired `thought`/`play`
2. Contact graph density over days
3. Host announcements vs islander actions that follow
4. `decisions.jsonl` traces for prompt/validation provenance
