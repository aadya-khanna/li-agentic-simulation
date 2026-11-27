# Run 091: `scheduled/minimal/cron-20261127-0753`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-27 |
| Condition | `minimal` |
| Seed | 2026112707 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261127-0753` |

## Headline arc

- **Day 1:** Baseline couples establish initial pairings (agent-1/agent-4, agent-2/agent-3, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters, steals agent-1, cascading into agent-4 stealing agent-2 and agent-3 getting dumped.
- **Day 5:** Bombshell agent-8 enters, steals agent-2, prompting agent-4 to steal agent-1 and leaving agent-7 dumped.
- **Day 6:** Unanimous islander vote saves agent-2, eliminating bombshell agent-8.
- **Day 7:** Unbroken Day-1 couple agent-5 and agent-6 win the season and £50,000.

## Insights

- **Baseline resilience:** Unlike recent runs where bombshell-integrated couples claimed victory, this run features an original Day-1 pair (agent-5/agent-6) surviving high-turnover interventions to take the prize.
- **Channel suppression parity:** The minimal condition again yields a strictly 0.0% whisper rate across 554 total events, forcing all tactical planning into public view.
- **Persistent model drag:** Flash-Lite logged 114 pass events (20.58% pass rate), highlighting systemic turn-taking execution friction.
- **Topological invariant:** Contact reciprocity remains stubbornly fixed at 1.0 despite substantial partner switching and bombshell disruptions.

## Limits

- Single-run observation ($n=1$) under a fixed seed prevents broader behavioral generalization.
- Complete absence of private whisper transcripts restricts communication analysis strictly to public channels.
- Progression relies on rigid, hard-coded milestone schedules rather than endogenous pacing.

## Next from this run

- [ ] Execute multi-seed batches under the minimal condition to measure the statistical distribution of Day-1 survivor winners versus mid-game recombination winners.
- [ ] Analyze prompt mechanics or engine loops driving the invariant 1.0 contact reciprocity score.
- [ ] Examine linguistic coordination markers in public transcripts leading up to the Day-6 unanimous islander vote for agent-2.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261127-0753
python scripts/brief_log.py --print
```
