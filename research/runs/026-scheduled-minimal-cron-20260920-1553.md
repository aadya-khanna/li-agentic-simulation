# Run 026: `scheduled/minimal/cron-20260920-1553`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-20 |
| Condition | `minimal` |
| Seed | 2026092015 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260920-1553` |

## Headline arc

- **Day 1:** Initial pairings form three baseline couples (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters and steals agent-2 from agent-1, leaving agent-1 single. Secondary shifts leave agent-6 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-4, leaving agent-3 single. Subsequent reshuffling leaves agent-1 dumped.
- **Day 6:** Public places agent-7 and agent-8 at risk; islander vote dumps agent-8.
- **Day 7:** Late-formed pairing agent-3 and agent-5 win the season and £50,000.

## Insights

- **Persistent zero-whisper execution:** Replicates prior runs with 0 whisper events out of 533 total actions, confirming total model reliance on public broadcast channels.
- **High conversational stalling:** A pass rate of 23.4% (125 pass events) demonstrates persistent generation friction and dialogue loops in the Flash Lite model.
- **Talk-winner disconnect:** The winning pair (agent-3 and agent-5) ranked only 4th in talk-winner contact metrics, reinforcing that high conversational volume does not drive victory outcomes.
- **Structural vulnerability at node-1:** Agent-1 experienced early displacement and ultimate elimination, mirroring recurring instability patterns around specific model initialization nodes.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents evaluation of tactical private subnets or secret alliances.
- Season progression remains strictly bounded by hard-coded schedule milestones.

## Next from this run

- - [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- - [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260920-1553
python scripts/brief_log.py --print
```
