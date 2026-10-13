# Run 048: `scheduled/minimal/cron-20261013-0630`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-13 |
| Condition | `minimal` |
| Seed | 2026101306 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261013-0630` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 steals agent-1, causing agent-4 to steal agent-6 and leaving agent-5 dumped.
- **Day 5:** Bombshell agent-8 steals agent-2, leaving agent-3 dumped; agent-4 and agent-6 formalize their winning partnership.
- **Day 6:** Islanders vote to save agent-7 and eliminate bombshell agent-8.
- **Day 7:** Surviving partners agent-4 and agent-6 win the season and £50,000.

## Insights

- **Absolute zero-whisper baseline:** Replicates total avoidance of private tactical subnets across all 581 events, maintaining a 0.0 whisper rate under the minimal condition.
- **Model generation friction:** A pass rate of 15.32% (89 pass events) highlights ongoing token emission constraints with the Flash Lite backend.
- **Talk-couple alignment convergence:** Unlike prior runs where conversational volume decoupled from survival, the winning pair (agent-4 and agent-6) also dominated conversational volume with 17 interactions.
- **High contact reciprocity:** The communication network maintained a reciprocity score of 1.0 despite high structural disruption and multiple partner switches.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261013-0630
python scripts/brief_log.py --print
```
