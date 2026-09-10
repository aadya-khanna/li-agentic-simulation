# Run 018: `scheduled/minimal/cron-20260910-1613`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-10 |
| Condition | `minimal` |
| Seed | 2026091016 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260910-1613` |

## Headline arc

- **Day 1:** Initial pairings formed (Agent 1 & Agent 2, Agent 3 & Agent 4, Agent 5 & Agent 6).
- **Day 3:** Bombshell Agent 7 enters, stealing Agent 1 from Agent 2; Agent 2 is dumped.
- **Day 5:** Bombshell Agent 8 enters, stealing Agent 3; Agent 4 pivots to steal Agent 1, leaving Agent 7 dumped.
- **Day 6:** Public vote exposes Agent 8 and Agent 1; islander vote dumps Agent 8.
- **Day 7:** Agent 1 & Agent 4 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates prior minimal runs with 0 whisper actions out of 531 events, confirming absolute reliance on public broadcast channels by Gemini Flash Lite.
- **Structural schedule dominance:** Elimination and survival outcomes remain entirely governed by hard-coded bombshell schedules rather than emergent relational pacing.
- **High conversational pass rate:** A pass rate of 24.7% (131 pass events) highlights persistent conversational stalling and loop tendencies within the model.
- **Dynamic partner shuffling:** Unlike previous runs where day-one pairs stayed intact, Agent 1 and Agent 4 successfully recombined mid-season to secure the win after bombshell disruptions.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private subnets.
- Season progression is strictly constrained by hard-coded schedule milestones.

## Next from this run

- - [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- - [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260910-1613
python scripts/brief_log.py --print
```
