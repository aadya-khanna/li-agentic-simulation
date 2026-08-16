# Experiment protocol

## Prompt conditions

| Condition | What agents receive |
|-----------|---------------------|
| `minimal` | Environment facts, observations, memory, visibility rules, allowed actions, ceremony constraints only |
| `incentive` | `minimal` plus factual prize and elimination consequences |

Default is `minimal`. There is no directive/narrative prompt layer.

## Commands

```bash
# Single local run (writes timestamped run under logs/experiments/local/minimal/)
python scripts/run_villa.py --stub --days 7 --condition minimal --seed 42

# Named experiment run
python scripts/run_villa.py --stub --days 1 --condition minimal --seed 1 \
  --experiment-id baseline-v1 --run-id seed-1

# Full condition matrix
python scripts/run_experiment.py harness/experiments/baseline.yaml

# Compare conditions
python harness/analysis/compare.py logs/experiments/baseline-v1

# Viewer (latest run)
python viewer/app.py

# Viewer (specific run)
python viewer/app.py --run-dir experiments/baseline-v1/minimal/seed-1
```

## Output layout

Every run writes to:

```
logs/experiments/<experiment_id>/<condition>/<run_id>/
  events.jsonl
  decisions.jsonl
  thoughts.jsonl
  brief.log
  state.json
  manifest.json
  metrics.json        # when run via run_experiment.py
```

`logs/latest.json` points at the most recently completed run.

## Interpretation limits

- `thought` and `play` are model self-reports, not verified cognition.
- Identical stub seed + config should produce identical tapes; live API runs may vary.
- Condition differences show prompt-treatment effects, not proof of human realism or training-data causation.
- Report distributions across seeds, not single entertaining seasons.

## Required repetitions

Run at least 3 seeds per condition before drawing conclusions. Use `summary.json` for mean/stdev comparison.
