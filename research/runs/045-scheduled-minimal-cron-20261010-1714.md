# Run 045: `scheduled/minimal/cron-20261010-1714`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-10 |
| Condition | `minimal` |
| Seed | 2026101017 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261010-1714` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, triggering a chain of swaps that leaves agent-4 dumped while agent-5/agent-6 remain stable.
- **Day 5:** Bombshell agent-8 enters and steals agent-7, leaving agent-2 dumped and forcing agent-7/agent-8 together.
- **Day 6:** Safe islanders vote to eliminate bombshell agent-8 over agent-7.
- **Day 7:** Original stable pair agent-5 and agent-6 win the season and £50,000.

## Insights

- **Stability selection:** The single undisturbed couple from Day 1 (agent-5/agent-6) successfully navigated the entire run without splitting, eventually winning the season.
- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 576 events, maintaining the 0.0 whisper rate characteristic of the minimal condition.
- **Model generation friction:** A pass rate of 18.4% (106 pass events) continues to indicate token emission constraints under the Flash Lite backend.
- **Islander voting consensus:** On Day 6, all surviving agents unanimously voted to save agent-7 and eliminate agent-8, reflecting high alignment in social exclusion mechanics.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Complete absence of private whisper logs restricts analysis exclusively to public broadcast interactions.
- Simulation progression remains strictly bound to hard-coded chronological milestones rather than emergent social pacing.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test winner-type distribution stability.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261010-1714
python scripts/brief_log.py --print
```
