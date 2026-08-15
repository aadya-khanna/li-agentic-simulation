# Tool: inspect logs

## Viewer (recommended)

```bash
python viewer/app.py
# http://127.0.0.1:8765
```

Toggle private thoughts, game-play, whispers, diary.

## CLI snippets

```bash
# Event count
wc -l logs/run.jsonl

# Last 5 events (pretty)
tail -5 logs/run.jsonl | python -m json.tool

# All recoupling picks
grep couple_choice logs/run.jsonl | python -m json.tool

# Thoughts with play field
grep '"kind": "thought"' logs/run.jsonl | head -3 | python -m json.tool
```

## Checkpoint fields

`logs/run-state.json` includes `islanders.<name>.contacts` (talk counts), `coupled_with`, `memories`, `inner_thoughts`.

## Analysis prompts

When comparing runs, diff:

1. Recoupling `text` + paired `thought`/`play`
2. Contact graph density over days
3. Host announcements vs islander actions that follow
