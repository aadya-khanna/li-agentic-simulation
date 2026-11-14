# Run 080: `scheduled/minimal/cron-20261114-1752`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-14 |
| Condition | `minimal` |
| Seed | 2026111417 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261114-1752` |

## Headline arc

- **Day 1:** Baseline pairings establish three couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-5, splitting agent-5/agent-6 and leaving agent-6 dumped; agent-1/agent-2 and agent-3/agent-4 preserve their pairings.
- **Day 5:** Bombshell agent-8 enters and steals agent-3, splitting agent-3/agent-4 and leaving agent-4 dumped; agent-5/agent-7 and agent-1/agent-2 remain paired.
- **Day 6:** Islanders vote to save agent-7 over agent-8, resulting in agent-8's elimination.
- **Day 7:** Unbroken Day-1 survivor couple agent-1 and agent-2 win the season and £50,000.

## Insights

- **Day-1 couple preservation:** Replicates previous minimal-condition runs where pairs surviving initial formation without disruption capture the season victory (agent-1/agent-2).
- **Absolute channel suppression:** Minimal condition maintains a strict 0.0% whisper rate across 603 events, completely eliminating private side-channels.
- **Topological tracking artifact:** Contact reciprocity remains pinned at 1.0 despite significant partner turnover, pointing to structural symmetry constraints in movement or logging.
- **Backend pacing overhead:** Model generation limits persist under the flash-lite configuration, reflected by 81 pass events (13.43% pass rate).

## Limits

- Single-run observation ($n=1$) bound to a specific random seed and prompt initialization.
- Complete absence of private whisper logs restricts structural communication analysis exclusively to public metrics.
- Narrative progression relies on hard-coded chronological milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to evaluate winner distribution variance when original pairs survive.
- [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261114-1752
python scripts/brief_log.py --print
```
