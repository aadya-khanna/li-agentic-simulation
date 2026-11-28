# Run 092: `scheduled/minimal/cron-20261128-0723`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-28 |
| Condition | `minimal` |
| Seed | 2026112807 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261128-0723` |

## Headline arc

- **Day 1:** Baseline couples establish initial pairings: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-3; agent-4 recovers by stealing agent-6 from agent-5, leaving agent-5 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-2; agent-1 steals agent-7, leaving agent-3 dumped.
- **Day 6:** Islanders vote to save agent-7, resulting in agent-8's elimination.
- **Day 7:** Recombined late-game partners agent-4 and agent-6 win the season and £50,000.

## Insights

- **Top-talk pair victory:** Unlike runs where original couples hold on, the top-talking pair by volume (agent-4 and agent-6, with 15 interactions) successfully claimed the season victory following their Day-3 recombination.
- **Zero whisper rate persistence:** Replicates the strict minimal condition pattern of a 0.0% whisper rate across 553 events, forcing all tactical planning entirely into public transcripts.
- **Persistent execution friction:** The Flash-Lite model logged 123 pass events (22.24% pass rate), highlighting systemic turn-taking drag.
- **Topological invariant:** Contact reciprocity remains locked at 1.0 despite high partner turnover, pointing to structural spatial constraints in the environment design.

## Limits

- Single-run observation ($n=1$) under a fixed random seed prevents broad behavioral generalization.
- Complete absence of private whisper transcripts restricts communication analysis exclusively to public channels.
- Progression relies on rigid, hard-coded milestone schedules rather than endogenous pacing.

## Next from this run

- [ ] Execute multi-seed batches under the minimal condition to measure the statistical distribution of top-talk pair winners versus baseline survivors.
- [ ] Analyze the prompt or turn-taking engine mechanics driving the invariant 1.0 contact reciprocity score.
- [ ] Examine linguistic coordination markers in public transcripts leading up to the Day-6 safe islander vote for agent-7.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261128-0723
python scripts/brief_log.py --print
```
