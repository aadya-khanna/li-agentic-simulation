# Run 053: `scheduled/minimal/cron-20261017-1522`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-17 |
| Condition | `minimal` |
| Seed | 2026101715 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261017-1522` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2 from agent-1, leaving agent-1 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-5 from agent-6, leaving agent-6 dumped.
- **Day 6:** Islanders vote to save agent-7 and eliminate bombshell agent-8.
- **Day 7:** Original baseline couple agent-3 and agent-4 win the season and £50,000.

## Insights

- **Baseline stability dominance:** Original couple agent-3 and agent-4 survived all interventions to win, aligning with high conversational volume (11 interactions).
- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 584 events, maintaining a 0.0 whisper rate.
- **High contact reciprocity:** The communication network maintained a reciprocity score of 1.0 despite structural disruption from bombshell arrivals.
- **Model generation friction:** A pass rate of 16.78% (98 pass events) continues to demonstrate token emission constraints with the Flash Lite backend.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261017-1522
python scripts/brief_log.py --print
```
