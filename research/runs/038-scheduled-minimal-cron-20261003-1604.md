# Run 038: `scheduled/minimal/cron-20261003-1604`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-03 |
| Condition | `minimal` |
| Seed | 2026100316 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261003-1604` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-1, leaving agent-2 dumped; agent-3/agent-4 and agent-5/agent-6 maintain their couplings.
- **Day 5:** Bombshell agent-8 enters and steals agent-5; agent-6 switches to agent-1, leaving bombshell agent-7 dumped.
- **Day 6:** Islander vote saves agent-5 and eliminates bombshell agent-8.
- **Day 7:** Original Day-1 pairing agent-3 and agent-4 maintain unbroken stability to win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 551 events, maintaining the 0.0 whisper rate characteristic of the minimal condition.
- **Anchor resilience vs. structural churn:** Day-1 pairing agent-3/agent-4 completely ignored external shocks from bombshells and subsequent cascades, mirroring winner durability seen in prior runs.
- **Model generation friction:** A pass rate of 21.05% (116 pass events) continues to demonstrate token emission constraints and loop limits under the Flash Lite backend.
- **Talk vs. couple network dissociation:** The top-talking pair (agent-3 and agent-5 with 9 interactions) did not couple or win, reinforcing that conversational frequency diverges from structural survival.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Complete absence of private whisper logs restricts analysis to public broadcast interactions only.
- Simulation progression remains strictly bound to hard-coded chronological milestones rather than emergent social pacing.

## Next from this run

- - [ ] Execute multi-seed batch runs for the minimal condition to test winner-type distribution stability.
- - [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- - [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261003-1604
python scripts/brief_log.py --print
```
