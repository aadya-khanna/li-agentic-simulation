# Run 079: `scheduled/minimal/cron-20261113-1929`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-13 |
| Condition | `minimal` |
| Seed | 2026111319 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261113-1929` |

## Headline arc

- **Day 1:** Initial pairings establish three baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-4, leaving agent-1 single; agent-1 subsequently pairs with agent-5 while agent-6 is dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-1, leaving agent-5 single and subsequently dumped, while agent-2/agent-3 and agent-4/agent-7 preserve their pairings.
- **Day 6:** Islanders vote to save agent-7 over agent-8, resulting in agent-8's elimination.
- **Day 7:** Stable original pairing agent-2 and agent-3 win the season and £50,000.

## Insights

- **Early stability bonus:** Replicates patterns where couples formed on Day 1 (agent-2/agent-3) insulate against mid-game disruption and capture the win.
- **Complete channel suppression:** Minimal condition maintains a strict 0.0% whisper rate across 580 events, eliminating private communications entirely.
- **Persistent topological artifact:** Contact reciprocity remains pinned at 1.0 despite high partner turnover, indicating systemic symmetry constraints in logging or movement.
- **Elevated backend overhead:** Model pacing limitations persist under the flash-lite configuration, reflected by 100 pass events (17.24% pass rate).

## Limits

- Single-run observation ($n=1$) bound to a specific random seed and prompt initialization.
- Complete absence of private whisper logs restricts structural communication analysis exclusively to public metrics.
- Narrative sequencing depends on hard-coded chronological triggers rather than endogenous behavioral pacing.

## Next from this run

- - [ ] Run multi-seed batches under the minimal condition to evaluate winner distribution variance when stable original pairs survive.
- - [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- - [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261113-1929
python scripts/brief_log.py --print
```
