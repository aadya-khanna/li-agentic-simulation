# Run 049: `scheduled/minimal/cron-20261013-1909`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-13 |
| Condition | `minimal` |
| Seed | 2026101319 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261013-1909` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-1; agent-4 steals agent-2, leaving agent-3 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-4, leaving agent-2 dumped while day-one pair agent-5/agent-6 remains untouched.
- **Day 6:** Islanders vote to save agent-7 and eliminate bombshell agent-8.
- **Day 7:** Day-one couple agent-5 and agent-6 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 566 events, maintaining a 0.0 whisper rate under the minimal condition.
- **Day-one pair survival:** Unlike runs where original couples dissolve completely, agent-5 and agent-6 maintained stability throughout the 7 days and secured the win.
- **Model generation friction:** A pass rate of 21.55% (122 pass events) continues to demonstrate token emission constraints with the Flash Lite backend.
- **Talk-couple alignment convergence:** The winning pair (agent-5 and agent-6) dominated conversational volume with 10 interactions, matching top-talk patterns seen in prior runs.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261013-1909
python scripts/brief_log.py --print
```
