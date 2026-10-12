# Run 047: `scheduled/minimal/cron-20261012-2110`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-12 |
| Condition | `minimal` |
| Seed | 2026101221 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261012-2110` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-6, and agent-4/agent-5.
- **Day 3:** Bombshell agent-7 enters and steals agent-6 from agent-3, leaving agent-3 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-7, triggering a secondary switch where agent-6 pairs with agent-2, leaving agent-1 dumped.
- **Day 6:** Surviving islanders vote unanimously to eliminate bombshell agent-8 over agent-7.
- **Day 7:** Cross-coupled survivors agent-2 and agent-6 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 569 events, maintaining the 0.0 whisper rate characteristic of the minimal condition.
- **Model generation friction:** A pass rate of 19.33% (110 pass events) continues to demonstrate token emission constraints under the Flash Lite backend.
- **Talk-couple alignment shift:** Unlike prior runs where talk frequency decoupled from survival, the winning pair (agent-2 and agent-6) also ranked highest in conversational volume (7 interactions).
- **High contact reciprocity:** The run achieved a contact reciprocity of 1.0 within its communication network despite multiple disruptive bombshell arrivals.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261012-2110
python scripts/brief_log.py --print
```
