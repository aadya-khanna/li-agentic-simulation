# Run 039: `scheduled/minimal/cron-20261004-1644`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-04 |
| Condition | `minimal` |
| Seed | 2026100416 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261004-1644` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-1; agent-2 switches to agent-6, leaving agent-5 dumped while agent-4 pivots to agent-3.
- **Day 5:** Bombshell agent-8 enters and steals agent-3, prompting agent-4 to pivot to agent-1, leaving bombshell agent-7 dumped.
- **Day 6:** Islander vote targets bombshell agent-8, resulting in elimination after public placement at risk.
- **Day 7:** Stable long-term conversational pair agent-2 and agent-6 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 569 events, maintaining the 0.0 whisper rate characteristic of minimal condition runs.
- **Talk-network alignment divergence:** Unlike prior runs where top talkers lost, the highest-interacting pair (agent-2 and agent-6 with 15 interactions) successfully coupled and won the season.
- **Model generation friction:** A pass rate of 18.98% (108 pass events) continues to demonstrate token emission constraints and loop limits under the Flash Lite backend.
- **Structural re-routing flexibility:** Agents readily abandon Day-1 pairings under bombshell pressure, maintaining high partner-switch counts (4 switches, 4 steals) driven entirely by environment scaffolding.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261004-1644
python scripts/brief_log.py --print
```
