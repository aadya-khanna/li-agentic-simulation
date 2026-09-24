# Run 030: `scheduled/minimal/cron-20260924-1657`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-24 |
| Condition | `minimal` |
| Seed | 2026092416 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260924-1657` |

## Headline arc

- **Day 1:** Baseline couples form (agent-1/agent-4, agent-2/agent-3, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters, steals agent-2 from agent-3; cascading switches pair agent-3 with agent-1 while agent-4 is dumped.
- **Day 5:** Bombshell agent-8 enters, steals agent-6 from agent-5; agent-5 switches to agent-1, leaving agent-3 dumped.
- **Day 6:** Public places bombshells agent-7 and agent-8 in the risk zone; islander vote eliminates agent-8.
- **Day 7:** Bombshell-anchored couple agent-2 and agent-7 win the season and £50,000.

## Insights

- **Structural zero-whisper persistence:** Replicates absolute avoidance of tactical private subnets, maintaining 0 whisper events across 601 total actions.
- **Bombshell-to-winner trajectory:** Unlike runs where original baseline pairs recover, an incoming bombshell (agent-7) successfully secures the victory after disrupting initial pairings.
- **Talk-volume divergence:** The winning pair (agent-2/agent-7) ranked 2nd in contact metrics, trailing the non-winning agent-5/agent-6 dyad, confirming conversation frequency does not guarantee success.
- **Model generation friction:** A 14.8% pass rate (89 pass events) underscores persistent dialogue looping and token emission stalls under the Flash Lite model.

## Limits

- Single-run observation ($n=1$) under specific stochastic and seed constraints.
- Absence of private whispers prevents analysis of hidden alliances or tactical communication.
- Progression remains tightly governed by hard-coded schedule milestones rather than autonomous agent strategy.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test bombshell win-rate stability.
- [ ] Force whisper usage via prompt constraints to test if communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260924-1657
python scripts/brief_log.py --print
```
