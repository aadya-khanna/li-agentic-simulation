# Run 087: `scheduled/minimal/cron-20261123-0706`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-23 |
| Condition | `minimal` |
| Seed | 2026112307 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261123-0706` |

## Headline arc

- **Day 1:** Initial pairings establish three baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-1, leaving agent-4 dumped; agent-5/agent-6 and agent-2/agent-3 preserve their partnerships.
- **Day 5:** Bombshell agent-8 enters and steals agent-2, leaving agent-3 single; agent-3 retaliates by stealing agent-1 from agent-7, leaving agent-7 dumped.
- **Day 6:** Islanders vote to save agent-1 over agent-8, resulting in agent-8's elimination.
- **Day 7:** Unbroken Day-1 survivor couple agent-5 and agent-6 win the season and £50,000.

## Insights

- **Day-1 survival premium:** Unlike recent runs featuring late-formation winners, this iteration rewards a persistently intact Day-1 pair (agent-5/agent-6) that avoided bombshell disruption throughout.
- **Absolute whisper suppression:** The minimal condition logs a strict 0.0% whisper rate (0 whispers across 559 events), entirely confining communication to public channels.
- **Invariant contact reciprocity:** Contact reciprocity remains fixed at 1.0 despite high partner turnover, pointing to an environment-driven topological artifact.
- **Execution friction overhead:** The Flash-Lite configuration generates 113 pass events (20.21% pass rate), highlighting persistent execution constraints during action phases.

## Limits

- Single-run observation ($n=1$) limited to a specific random seed and prompt configuration.
- Absence of private whisper logs restricts communication analysis strictly to public transcripts.
- Progression relies on hard-coded milestone triggers rather than endogenous pacing.

## Next from this run

- - [ ] Run multi-seed batches under the minimal condition to test whether Day-1 survival advantage holds across diverse random seeds.
- - [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varying network topologies.
- - [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261123-0706
python scripts/brief_log.py --print
```
