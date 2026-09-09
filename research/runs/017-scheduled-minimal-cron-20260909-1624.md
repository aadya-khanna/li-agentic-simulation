# Run 017: `scheduled/minimal/cron-20260909-1624`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-09 |
| Condition | `minimal` |
| Seed | 2026090916 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260909-1624` |

## Headline arc

- **Day 1:** Initial pairings formed (Agent 1 & Agent 2, Agent 3 & Agent 4, Agent 5 & Agent 6).
- **Day 3:** Bombshell Agent 7 enters, stealing Agent 2; Agent 1 is left single and dumped.
- **Day 5:** Bombshell Agent 8 enters, stealing Agent 5; Agent 6 is left single and dumped.
- **Day 6:** Public vote places Agents 7 and 8 at risk; islander vote results in Agent 8 being dumped.
- **Day 7:** Agent 3 & Agent 4 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates prior minimal runs with exactly 0 whisper actions (out of 547 total events), indicating that Gemini Flash Lite relies entirely on public broadcast channels.
- **Structural schedule dominance:** Elimination and survival outcomes remain strictly governed by hard-coded bombshell schedules rather than emergent relational pacing.
- **High pass rate behavior:** A pass rate of 21.9% (120 pass events) highlights conversational stalling or repetitive loop tendencies within the model.
- **Model prior leakage:** Stable long-term survival of initial pairs (Agent 3 & Agent 4) points to default safe-routing behavior in generic LLM configurations.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private subnets.
- Season progression is entirely constrained by hard-coded schedule milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260909-1624
python scripts/brief_log.py --print
```
