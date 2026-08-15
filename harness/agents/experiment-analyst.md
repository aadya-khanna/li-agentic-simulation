# Subagent: experiment-analyst

**Use when:** interpreting a run, comparing conditions, or designing eval metrics — not implementing engine code.

## Inputs

- `logs/run.jsonl` — full event tape
- `logs/run-state.json` — final checkpoint
- `logs/thoughts.jsonl` — private thoughts only

## Questions to answer

1. Where does `thought` diverge from `play` on the same beat?
2. Who spoke to whom (`contacts` in checkpoint, or infer from speak/whisper/huddle events)?
3. At recoupling, who picked someone already in a couple? What was their `play` field?
4. Did behaviour change day-over-day with empty vs full major moments?

## Tools

- Viewer: `python viewer/app.py` → http://127.0.0.1:8765
- CLI recap: run season with `--stub` or `--live` and read terminal output
- See `harness/tools/inspect-logs.md`

## Do not

- Change prompts to "fix" interesting emergent behaviour without explicit research ask
- Treat stub output as live-model conclusions
