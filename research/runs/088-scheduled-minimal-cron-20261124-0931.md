# Run 088: `scheduled/minimal/cron-20261124-0931`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-24 |
| Condition | `minimal` |
| Seed | 2026112409 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261124-0931` |

## Headline arc

- **Day 1:** Three baseline couples establish initial pairings: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-1 dumped; agent-5/agent-6 and agent-3/agent-4 preserve their partnerships.
- **Day 5:** Bombshell agent-8 enters and steals agent-7, leaving agent-2 single; agent-2 retaliates by stealing agent-4 from agent-3, leaving agent-3 dumped.
- **Day 6:** Islanders vote to save agent-7, resulting in agent-8's elimination.
- **Day 7:** Intact Day-1 survivor couple agent-5 and agent-6 win the season and £50,000.

## Insights

- **Day-1 persistence validation:** Replicates the Run 087 pattern where an unbroken Day-1 pair (agent-5/agent-6) secures victory, contrasting with mid-game bombshell restructuring seen in Run 086.
- **Zero whisper baseline maintenance:** Confirms absolute structural suppression of private channels under the minimal prompt condition (0.0% whisper rate across 591 events).
- **Topological invariant artifact:** Contact reciprocity remains locked at 1.0 despite high partner turnover and structural shocks, signaling environment-driven spatial constraints.
- **Action execution friction:** Flash-Lite configuration generates 103 pass events (17.43% pass rate), demonstrating persistent execution overhead during turn-taking phases.

## Limits

- Single-run observation ($n=1$) bound to a specific random seed and prompt structure.
- Total absence of private whisper data restricts conversational analysis entirely to public transcripts.
- Progression relies on hard-coded milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to test whether Day-1 survival advantage holds across diverse random seeds.
- [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varying network topologies.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261124-0931
python scripts/brief_log.py --print
```
