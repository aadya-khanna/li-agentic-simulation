# Run 031: `scheduled/minimal/cron-20260925-1700`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-25 |
| Condition | `minimal` |
| Seed | 2026092517 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260925-1700` |

## Headline arc

- **Day 1:** Baseline couples form with agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-3, leaving agent-4 dumped; agent-1 and agent-2 secure the first hideaway date.
- **Day 5:** Bombshell agent-8 enters and steals agent-5, while agent-6 retaliates by pairing with agent-3; bombshell agent-7 is dumped.
- **Day 6:** Public places agent-3 and agent-8 in the risk zone; subsequent islander votes eliminate agent-3.
- **Day 7:** Original Day-1 surviving couple agent-1 and agent-2 win the season and £50,000.

## Insights

- **Day-1 resilience validation:** Unlike prior runs where bombshells usurp the crown, the original agent-1/agent-2 pairing persists through multiple structural shocks to claim victory, aligning with high talk volumes.
- **Absolute zero-whisper replication:** Replicates prior minimal condition runs with 0 whisper actions across 533 total events, showing a complete structural avoidance of private subnets.
- **Persistent generation friction:** A high pass rate of 24.5% (131 pass events) highlights ongoing token emission stalls and dialogue looping under the Flash Lite model.
- **Deterministic schedule constraints:** Villa progression remains strictly anchored to hard-coded bombshell entrances and forced recouplings rather than emergent autonomous strategies.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Complete absence of private whisper logs prevents evaluation of hidden tactical alliances.
- Progression is heavily gated by rigid scheduling rather than dynamic social feedback loops.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test winner-type distribution stability.
- [ ] Force whisper usage via prompt constraints to test if communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260925-1700
python scripts/brief_log.py --print
```
