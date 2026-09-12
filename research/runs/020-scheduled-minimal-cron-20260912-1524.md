# Run 020: `scheduled/minimal/cron-20260912-1524`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-12 |
| Condition | `minimal` |
| Seed | 2026091215 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260912-1524` |

## Headline arc

- **Day 1:** Initial baseline pairings lock in three couples (1-2, 3-4, 5-6).
- **Day 3:** Bombshell agent-7 enters, steals agent-2, triggering cascading swaps that result in agent-4 being dumped.
- **Day 5:** Bombshell agent-8 enters and disrupts couplings further; agent-1 and agent-5 pair up while agent-6 is dumped.
- **Day 6:** Public puts agent-8 and agent-7 at risk; islander vote eliminates agent-8.
- **Day 7:** Agent-2 and agent-3 secure the final win and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates prior runs with 0 whisper actions out of 561 events, confirming absolute reliance on public broadcast channels by Gemini Flash Lite.
- **Structural schedule dominance:** Elimination and survival outcomes remain entirely governed by hard-coded milestone triggers rather than emergent relational pacing.
- **High conversational pass rate:** A pass rate of 20.3% (114 pass events) highlights persistent conversational stalling and loop tendencies within the model.
- **Divergent talk vs. couple networks:** Top talk pairs (e.g., agent-2/agent-7 with 15 events) failed to translate into winning partnerships, as agent-2 ultimately won with agent-3 despite lower direct interaction volume.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private subnets.
- Season progression is strictly constrained by hard-coded schedule milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260912-1524
python scripts/brief_log.py --print
```
