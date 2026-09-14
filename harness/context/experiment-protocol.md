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

# Full condition matrix (7-day replication — preferred for thesis claims)
python scripts/run_experiment.py harness/experiments/replication.yaml

# Smoke matrix (1-day stub only)
python scripts/run_experiment.py harness/experiments/baseline.yaml

# Re-aggregate metrics after runs exist
python harness/analysis/compare.py logs/experiments/replication-v1

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
  metrics.json              # structural + replication battery
  replication_summary.json  # seed aggregation (experiment root only)
```

`logs/latest.json` points at the most recently completed run.

Metric definitions and reporting rules: [`replication-metrics.md`](replication-metrics.md).

## Interpretation limits

- `thought` and `play` are model self-reports, not verified cognition.
- Identical stub seed + config should produce identical tapes; live API runs may vary.
- Condition differences show prompt-treatment effects, not proof of human realism or training-data causation.
- Report distributions across seeds, not single entertaining seasons.

## Required repetitions

Run at least **3 seeds per condition** before drawing conclusions. Use `replication_summary.json` for thesis-facing rates (mean/stdev, invariants, readiness gate). Do not cite single cron seasons as evidence.
