# Run 050: `scheduled/minimal/cron-20261014-1658`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-14 |
| Condition | `minimal` |
| Seed | 2026101416 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261014-1658` |

## Headline arc

- **Day 1:** Baseline couples established: agent-1/agent-4, agent-2/agent-3, agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters, steals agent-3 from agent-2, leaving agent-2 dumped; original pair agent-1/agent-4 and agent-5/agent-6 remain locked.
- **Day 5:** Bombshell agent-8 enters, steals agent-3 from agent-7, while agent-6 drops agent-5 to steal/couple with agent-7, leaving agent-5 dumped; agent-1/agent-4 stay untouched and secure a private hideaway date.
- **Day 6:** Islanders vote to save agent-7 and eliminate bombshell agent-8.
- **Day 7:** Persistent day-one couple agent-1 and agent-4 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 569 events, maintaining a 0.0 whisper rate under the minimal condition.
- **Top-talk pair winner convergence:** The winning pair (agent-1 and agent-4) also dominated conversational volume with 9 interactions, matching top-talk patterns observed in prior runs.
- **High contact reciprocity:** The communication network maintained a reciprocity score of 1.0 despite high structural disruption and bombshell interventions.
- **Model generation friction:** A pass rate of 17.93% (102 pass events) continues to demonstrate token emission constraints with the Flash Lite backend.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261014-1658
python scripts/brief_log.py --print
```
