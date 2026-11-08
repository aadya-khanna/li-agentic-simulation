# Run 074: `scheduled/minimal/cron-20261108-1751`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-08 |
| Condition | `minimal` |
| Seed | 2026110817 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261108-1751` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 steals agent-6, leaving agent-5 dumped while agent-1/agent-2 and agent-3/agent-4 maintain their pairings.
- **Day 5:** Bombshell agent-8 steals agent-3, leaving agent-4 single; agent-4 then pivots to couple with agent-7, resulting in agent-6 being dumped.
- **Day 6:** Safe islanders vote to eliminate bombshell agent-8 after a public risk designation.
- **Day 7:** Original Day-1 survival couple agent-1 and agent-2 win the season and £50,000.

## Insights

- **Day-1 survival dominance:** Replicates previous patterns where original, uninterrupted pairs (agent-1/agent-2) successfully navigate mid-season bombshell disruptions to claim the win.
- **Absolute public channel constraint:** Maintains a 0.0% whisper rate across 563 events, strictly confining dialogue to public broadcast spaces under the minimal condition.
- **Artificial reciprocity artifact:** Contact reciprocity locks completely at 1.0 despite multiple partner steals and structural churn.
- **Significant generation friction:** Backend model exhibits high token generation overhead with a 19.89% pass rate (112 pass events), indicating persistent behavioral pacing limits.

## Limits

- Single-run observation ($n=1$) restricted to a specific random seed and prompt environment.
- Complete absence of private whisper logs restricts structural communication analysis to public dialogue.
- Progression relies on hard-coded chronological milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to evaluate winner distribution variance when original pairs survive.
- [ ] Enforce whisper constraints via prompt engineering to test whether communication topologies diverge from 100% public broadcast.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261108-1751
python scripts/brief_log.py --print
```
