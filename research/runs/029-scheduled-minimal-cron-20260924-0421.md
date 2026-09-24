# Run 029: `scheduled/minimal/cron-20260924-0421`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-24 |
| Condition | `minimal` |
| Seed | 2026092404 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260924-0421` |

## Headline arc

- **Day 1:** Initial baseline couples established (agent-1/agent-4, agent-2/agent-3, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters, steals agent-2; cascading switches leave agent-3 pairing with agent-1 while agent-4 is dumped.
- **Day 5:** Bombshell agent-8 enters, steals agent-5; subsequent shifts reunite original partners agent-2 and agent-3, while bombshell agent-7 is dumped.
- **Day 6:** Islander vote eliminates agent-8 after landing in the public risk zone alongside agent-1.
- **Day 7:** Reunited Day-1 couple agent-2 and agent-3 win the season and £50,000.

## Insights

- **Persistent zero-whisper execution:** Replicates prior minimal runs with 0 whisper actions out of 561 total events, showing a total structural reliance on public broadcast channels.
- **Ongoing generation friction:** A 18.7% pass rate (105 pass events) points to persistent dialogue loops and generation stalling within the Flash Lite model.
- **Reunion resilience:** The winning couple (agent-2 and agent-3) successfully reformed after structural disruptions on Day 3, demonstrating that early baseline pairing dynamics can recover post-bombshell.
- **Environment-driven flow:** Villa narrative pacing remains entirely tethered to hard-coded bombshell schedules and forced recoupling mechanics rather than autonomous strategic maneuvering.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Absolute absence of private whisper communication prevents evaluation of tactical subnets or secret alliances.
- Progression remains rigidly anchored to hard-coded schedule milestones.

## Next from this run

- - [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- - [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260924-0421
python scripts/brief_log.py --print
```
