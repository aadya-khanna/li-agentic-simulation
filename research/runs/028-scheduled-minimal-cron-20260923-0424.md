# Run 028: `scheduled/minimal/cron-20260923-0424`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-23 |
| Condition | `minimal` |
| Seed | 2026092304 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260923-0424` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters, steals agent-4, triggering cascading switches that leave agent-3 pairing with agent-1 and agent-2 with agent-5; agent-6 is dumped.
- **Day 5:** Bombshell agent-8 enters, steals agent-7; agent-1 and agent-3 reaffirm their pairing while agent-4 is dumped.
- **Day 6:** Public places agent-7 and agent-8 in the risk zone; islander vote eliminates agent-8.
- **Day 7:** Cross-initial pairing agent-1 and agent-3 win the season and the £50,000 prize.

## Insights

- **Persistent zero-whisper execution:** Replicates prior runs with 0 whisper events out of 543 total actions, proving total reliance on public broadcast channels.
- **Conversational stalling persists:** A 22.8% pass rate (124 pass events) indicates ongoing generation friction and model-level dialogue loops in Flash Lite.
- **Talk-winner disconnect:** The winning couple (agent-1 and agent-3) ranked 5th in talk-winner contact metrics, reinforcing that conversational volume fails to predict simulation success.
- **Structural environment dominance:** Narrative trajectory is heavily dictated by hard-coded bombshell schedules and forced recoupling mechanics rather than emergent strategy.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents evaluation of tactical private subnets or secret alliances.
- Season progression remains rigidly anchored to hard-coded schedule milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260923-0424
python scripts/brief_log.py --print
```
