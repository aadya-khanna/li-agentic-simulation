# Run 085: `scheduled/minimal/cron-20261121-1859`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-21 |
| Condition | `minimal` |
| Seed | 2026112118 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261121-1859` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-5, forcing agent-6 to switch to agent-2 while agent-3 is dumped; agent-1/agent-4 preserve their partnership.
- **Day 5:** Bombshell agent-8 enters and steals agent-2, prompting agent-6 to switch to agent-5 while agent-7 is dumped.
- **Day 6:** Islanders vote to save agent-5 over agent-8, resulting in agent-8's elimination.
- **Day 7:** Unbroken Day-1 survivor couple agent-1 and agent-4 win the season and £50,000.

## Insights

- **Day-1 stability premium:** Replicates structural patterns where an intact Day-1 couple surviving successive bombshell shocks captures the season victory.
- **Absolute whisper suppression:** The minimal condition maintains a strict 0.0% whisper rate (0 whispers across 574 events), blocking private side-channel communication entirely.
- **Invariant spatial symmetry:** Contact reciprocity remains pinned at 1.0 regardless of partner turnover, reflecting a persistent environment-driven artifact.
- **Persistent generation overhead:** Flash-lite configuration yields 104 pass events (18.12% pass rate), signaling consistent execution friction during action selection.

## Limits

- Single-run observation ($n=1$) constrained to a specific random seed and prompt setting.
- Absence of private whisper logs restricts structural communication analysis exclusively to public channels.
- Chronological progression relies on hard-coded milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- - [ ] Run multi-seed batches under the minimal condition to quantify winner survival variance when Day-1 pairs remain intact.
- - [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- - [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261121-1859
python scripts/brief_log.py --print
```
