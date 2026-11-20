# Run 084: `scheduled/minimal/cron-20261120-1954`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-20 |
| Condition | `minimal` |
| Seed | 2026112019 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261120-1954` |

## Headline arc

- **Day 1:** Three baseline couples form: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-5, leaving agent-6 single and dumped, while other pairs hold.
- **Day 5:** Bombshell agent-8 enters and steals agent-4, triggering a cascading re-pairing chain that links agent-1 with agent-3 and eliminates agent-7.
- **Day 6:** Islanders vote to save agent-5 over agent-8, resulting in agent-8's elimination.
- **Day 7:** Late-formed non-Day-1 pair agent-1 and agent-3 win the season and £50,000.

## Insights

- **Late-stage reorganization triumph:** Replicates the pattern from run 082 where non-Day-1 survivor pairs formed via structural shocks secure the season win, contrasting with early-run baseline survivals.
- **Absolute communication bottleneck:** The minimal condition maintains a strict 0.0% whisper rate (0 whispers across 583 events), restricting all discourse strictly to public spaces.
- **Invariant topological symmetry:** Contact reciprocity remains fixed at 1.0 despite high partner turnover (4 switches), indicating underlying spatial tracking artifacts.
- **Persistent generation friction:** Flash-lite configuration generates 102 pass events (17.5% pass rate), highlighting continuous execution constraints during action phases.

## Limits

- Single-run observation ($n=1$) under a fixed random seed and prompt condition.
- Absence of private whisper logs limits network analysis exclusively to public dialogue.
- Chronological progression relies on hard-coded milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to quantify winner survival variance when Day-1 couples are disrupted.
- [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261120-1954
python scripts/brief_log.py --print
```
