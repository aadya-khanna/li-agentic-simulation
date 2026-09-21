# Run 027: `scheduled/minimal/cron-20260921-1808`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-21 |
| Condition | `minimal` |
| Seed | 2026092118 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260921-1808` |

## Headline arc

- **Day 1:** Initial pairings establish three baseline couples (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-1 single; agent-1 retaliates by stealing agent-4, dumping agent-3.
- **Day 5:** Bombshell agent-8 enters and steals agent-1, leaving agent-4 dumped while agent-5 and agent-6 remain stable.
- **Day 6:** Islander vote eliminates bombshell agent-8 after landing in the public risk zone alongside agent-7.
- **Day 7:** Stable original pairing agent-5 and agent-6 win the season and the £50,000 prize.

## Insights

- **Persistent zero-whisper execution:** Confirms complete reliance on public broadcast channels with 0 whisper actions out of 554 total events, matching prior runs.
- **Conversational stalling remains high:** A pass rate of 21.8% (121 pass events) highlights ongoing generation friction and dialogue loops in the Flash Lite model.
- **Stability over disruption:** The winning pair (agent-5 and agent-6) survived intact from Day 1 without participating in partner switches, demonstrating that staying unperturbed outranks active maneuvering.
- **Talk-winner disconnect:** The winning couple ranked 16th in talk-winner contact metrics, further proving that conversational volume does not predict simulation success.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Absolute absence of whisper communication prevents evaluation of tactical private subnets or secret alliances.
- Season progression remains rigidly anchored to hard-coded schedule milestones.

## Next from this run

- - [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- - [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260921-1808
python scripts/brief_log.py --print
```
