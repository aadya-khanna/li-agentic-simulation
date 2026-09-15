# Replication metrics

Structural metrics from a **single run** are anecdotes. The replication battery turns a seed matrix into **distributional evidence** the thesis can cite.

## Thesis mapping

| Metric | Research question (from `research-goals.md`) |
|--------|-----------------------------------------------|
| `day1_winner` | Do early couplings survive ceremony pressure and win? (loyalty vs game) |
| `day1_couple_survival` | What fraction of Day-1 pairs are still coupled at finale? |
| `top_talk_pair_is_winner` | Does the heaviest talk edge predict the winning couple? |
| `talk_winner_contact_rank` | Rank of winner pair in the contact graph (1 = most talked-to) |
| `contact_density` / `contact_reciprocity` | Social graph shape from `contacts` (no relationship maths) |
| `partner_switches` / `steal_count` / `steal_pick_rate` | Recoupling churn when couples already exist |
| `claim_evidence_gap_rate` | Recoupling speech claims connection vs pre-pick talk count |
| `whisper_rate` / `whisper_count` | Private-channel use (asymmetric information) |
| `pass_rate` | Conversational stalling vs engagement |
| `gather_count` | Agent-initiated social structure (endogenous events) |
| `fallback_count` | Engine corrections — exclude from emergence claims when >0 |

## Per-run output

Every run that calls `write_metrics()` gets `metrics.json` with:

- **Top-level scalars** — backward-compatible flat keys (`pass_rate`, `partner_switches`, …).
- **`replication` block** — thesis-facing fields including `day1_couples`, `winner_couple`, and the battery above.

## Aggregation (multi-seed)

```bash
# Run a matrix (writes metrics.json per run + summaries)
python scripts/run_experiment.py harness/experiments/replication.yaml

# Re-aggregate if runs already exist
python harness/analysis/compare.py logs/experiments/replication-v1
```

Writes:

| File | Contents |
|------|----------|
| `summary.json` | Mean/stdev/n for all numeric metrics (legacy) |
| `replication_summary.json` | Battery-only stats, invariants, readiness gate, condition contrasts |

### Readiness gate

A condition is **`ready`** when:

1. **n ≥ 3** completed runs with `metrics.json`.
2. Each battery metric reports `mean`, `stdev`, and raw `values`.

Do **not** treat single cron seasons as conclusions. Cron notes are pilots; the replication matrix is the evidence layer.

### Invariants

When `stdev == 0` across seeds (e.g. `whisper_count` always 0 under Gemini Flash Lite), the summary flags **`invariant: true`**. That is a reproducible finding, not missing variance — but it means that lever is saturated and needs an ablation (forced whisper, different model) before claiming private-channel behaviour.

### Condition contrasts

When both `minimal` and `incentive` meet `min_n`, `replication_summary.json` includes `contrasts.incentive_vs_minimal` with mean deltas for each battery metric. Interpret as **prompt-treatment effect**, not ground truth about humans.

## Recommended matrix

See `harness/experiments/replication.yaml`:

- **7 days** (full schedule — bombshells, vote, finale)
- **Seeds** `{42, 43, 44}` minimum; expand to `{42..46}` before writing up
- **Conditions** `minimal` and `incentive` (paired comparison on same seeds)

Stub first for harness parity; promote to live when comparing models.

```bash
python scripts/run_experiment.py harness/experiments/replication-live.yaml --live --stub-on-error
```

## Reporting template

When citing results:

> Across **n=3** minimal seeds, **`day1_winner`** occurred in **2/3** runs (mean 0.67 ± 0.47). **`whisper_count`** was **invariant at 0**. **`claim_evidence_gap_rate`** averaged **0.42 ± 0.12** (recoupling rhetoric ahead of contact logs).

Never report a single cron run as a rate.
