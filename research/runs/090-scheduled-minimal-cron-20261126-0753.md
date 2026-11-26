# Run 090: `scheduled/minimal/cron-20261126-0753`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-26 |
| Condition | `minimal` |
| Seed | 2026112607 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261126-0753` |

## Headline arc

- **Day 1:** Three baseline couples form: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters, steals agent-2, triggering a cascade where agent-3 steals agent-1 and agent-4 steals agent-6; agent-5 is dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-4, leaving agent-6 dumped; agent-1/agent-3 and agent-2/agent-7 remain paired.
- **Day 6:** Islanders vote to save agent-7, resulting in agent-8's elimination.
- **Day 7:** Recombined late-game partners agent-1 and agent-3 win the season and £50,000.

## Insights

- **Mid-game recombination victory:** Unlike runs where initial pairings dominate, this run demonstrates that a couple formed via cascading post-bombshell steals (agent-1/agent-3) can successfully claim victory.
- **Zero whisper suppression:** Replicates the strict minimal condition pattern of 0.0% whisper rates, forcing all tactical negotiations into public transcripts.
- **Persistent model friction:** The Flash-Lite backend logged 100 pass events (17.83% pass rate), signaling ongoing turn-taking execution drag.
- **Topological invariant:** Contact reciprocity remains rigidly fixed at 1.0 despite high partner turnover, pointing to structural spatial constraints in the environment setup.

## Limits

- Single-run observation ($n=1$) under a fixed random seed prevents broad behavioral generalization.
- Complete absence of private whisper transcripts restricts communication analysis exclusively to public channels.
- Progression relies on rigid, hard-coded milestone schedules rather than endogenous pacing.

## Next from this run

- [ ] Execute multi-seed batches under the minimal condition to measure the statistical distribution of mid-game recombination winners versus baseline survivors.
- [ ] Analyze the prompt or turn-taking engine mechanics driving the invariant 1.0 contact reciprocity score.
- [ ] Examine linguistic coordination markers in public transcripts leading up to the Day-6 safe islander vote.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261126-0753
python scripts/brief_log.py --print
```
