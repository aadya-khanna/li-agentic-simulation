# Run 046: `scheduled/minimal/cron-20261011-1737`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-11 |
| Condition | `minimal` |
| Seed | 2026101117 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261011-1737` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-1, triggering a cascade where agent-6 steals agent-2, leaving agent-5 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-4, prompting a series of swaps that leaves agent-7 dumped and forms the final winning couple.
- **Day 6:** Surviving islanders vote to eliminate bombshell agent-8.
- **Day 7:** Cross-coupled survivors agent-3 and agent-6 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 578 events, maintaining the 0.0 whisper rate characteristic of the minimal condition.
- **Model generation friction:** A pass rate of 15.92% (92 pass events) continues to highlight token emission constraints under the Flash Lite backend.
- **Talk-to-couple divergence:** The winning couple (agent-3 and agent-6) ranked 6th in talk frequency (7 interactions), reinforcing prior findings that conversational volume does not reliably predict structural survival.
- **High contact reciprocity:** Despite high restructuring and multiple partner switches, the run achieved a contact reciprocity of 1.0 within its communication network.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261011-1737
python scripts/brief_log.py --print
```
