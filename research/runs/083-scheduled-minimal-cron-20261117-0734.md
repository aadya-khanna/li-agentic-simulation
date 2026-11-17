# Run 083: `scheduled/minimal/cron-20261117-0734`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-17 |
| Condition | `minimal` |
| Seed | 2026111707 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261117-0734` |

## Headline arc

- **Day 1:** Initial pairings establish three baseline couples: agent-1/agent-2, agent-3/agent-6, and agent-4/agent-5.
- **Day 3:** Bombshell agent-7 enters and steals agent-3, triggering cascading switches that leave agent-2 dumped while agent-4/agent-5 preserve their Day-1 partnership.
- **Day 5:** Bombshell agent-8 enters and steals agent-6, forcing further re-pairings that eliminate agent-7 and leave agent-1/agent-3 newly partnered.
- **Day 6:** Islanders vote to save agent-4 over agent-8, resulting in agent-8's elimination from the villa.
- **Day 7:** Unbroken Day-1 survivor couple agent-4 and agent-5 win the season and £50,000.

## Insights

- **Day-1 resilience advantage:** Replicates prior runs showing that a couple formed on Day 1 surviving structural shocks (agent-4/agent-5) captures the season victory.
- **Absolute whisper suppression:** Minimal condition maintains a strict 0.0% whisper rate across 565 events, entirely blocking private side-channel communication.
- **Invariant topological metrics:** Contact reciprocity remains pinned at 1.0 despite high partner turnover, reflecting persistent spatial symmetry artifacts.
- **Generation pacing overhead:** Flash-lite configuration yields 104 pass events (18.41% pass rate), signaling ongoing execution constraints during action selection.

## Limits

- Single-run observation ($n=1$) bound to a specific random seed and prompt condition.
- Lack of private whisper logs restricts structural communication analysis exclusively to public channels.
- Chronological progression depends on hard-coded milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- - [ ] Run multi-seed batches under the minimal condition to test winner survival variance when Day-1 pairs remain intact.
- - [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- - [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261117-0734
python scripts/brief_log.py --print
```
