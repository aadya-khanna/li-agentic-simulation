# Run 082: `scheduled/minimal/cron-20261116-2152`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-16 |
| Condition | `minimal` |
| Seed | 2026111621 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261116-2152` |

## Headline arc

- **Day 1:** Three baseline couples establish initial pairings: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-5, forcing cascading switches that leave agent-1 dumped and new pairs formed.
- **Day 5:** Bombshell agent-8 enters and steals agent-5, triggering further re-pairings that eliminate agent-7 and leave agent-4 and agent-6 newly partnered.
- **Day 6:** Remaining islanders vote to save agent-4 over agent-8, resulting in agent-8's elimination.
- **Day 7:** Non-Day-1 survivor couple agent-4 and agent-6 win the season and £50,000.

## Insights

- **Divergence from prior survival patterns:** Unlike runs 080 and 081 where unbroken Day-1 pairs won, this run's winners (agent-4/agent-6) formed through late-stage structural reorganization after prior partner disruption.
- **Zero private communication ceiling:** The minimal condition again produces a strict 0.0% whisper rate (0 whispers across 578 events), restricting all interaction to public channels.
- **Persistent topological artifacts:** Contact reciprocity remains pinned at 1.0 despite high partner turnover, reflecting persistent symmetry constraints in spatial tracking.
- **Model execution friction:** Flash-lite configuration yields 95 pass events (16.44% pass rate), highlighting ongoing generation pacing constraints.

## Limits

- Single-run observation ($n=1$) under a specific random seed and prompt condition.
- Absence of private whisper logs limits network analysis entirely to public dialogue and proximity.
- Chronological progression relies on hard-coded milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to quantify winner survival variance when Day-1 couples are disrupted.
- [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261116-2152
python scripts/brief_log.py --print
```
