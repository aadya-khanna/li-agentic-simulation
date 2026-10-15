# Run 051: `scheduled/minimal/cron-20261015-1645`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-15 |
| Condition | `minimal` |
| Seed | 2026101516 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261015-1645` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2 from agent-1; agent-1 steals agent-3 from agent-4, leaving agent-4 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-6 from agent-5; agent-5 steals agent-1 from agent-3, leaving agent-3 dumped.
- **Day 6:** Islanders vote to save agent-7 and eliminate bombshell agent-8.
- **Day 7:** Cross-network couple agent-1 and agent-5 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 580 events, maintaining a 0.0 whisper rate under the minimal condition.
- **High contact reciprocity:** The communication network maintained a reciprocity score of 1.0 despite high structural disruption and bombshell interventions.
- **Model generation friction:** A pass rate of 19.66% (114 pass events) continues to demonstrate token emission constraints with the Flash Lite backend.
- **Divergence from top-talk winner convergence:** Unlike prior runs where top-talk pairs won, the winning pair (agent-1 and agent-5) ranked second in conversational volume (7 interactions), behind agent-6 and agent-8 (9 interactions).

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261015-1645
python scripts/brief_log.py --print
```
