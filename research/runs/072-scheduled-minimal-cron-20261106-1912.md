# Run 072: `scheduled/minimal/cron-20261106-1912`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-06 |
| Condition | `minimal` |
| Seed | 2026110619 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261106-1912` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-1 dumped; agent-3/agent-4 and agent-5/agent-6 maintain their pairings.
- **Day 5:** Bombshell agent-8 enters and steals agent-6, causing agent-4 to drop agent-3 and couple with agent-5, while agent-3 is dumped.
- **Day 6:** Safe islanders vote to eliminate bombshell agent-8.
- **Day 7:** Cross-original pairing agent-4 and agent-5 win the season and £50,000.

## Insights

- **Emergence of cross-pairing winners:** Unlike prior runs where original day-1 survival couples swept the win, this run features a winning pair (agent-4 and agent-5) formed via a mid-season partner switch following bombshell disruptions.
- **Invariable private channel absence:** Replicates a 0.0% whisper rate across 570 events, confirming that the minimal prompt condition restricts all communication entirely to public broadcast channels.
- **Rigid network reciprocity:** Contact reciprocity remains artificially locked at 1.0 despite dynamic partner steals and structural changes.
- **Token generation friction:** The model backend maintains a high pass rate (19.47%, 111 pass events), highlighting ongoing technical overhead and generation pacing constraints.

## Limits

- Single-run observation ($n=1$) constrained to a specific random seed and prompt environment.
- Total absence of private whisper logs limits social network analysis strictly to public dialog channels.
- System progression relies on hard-coded chronological milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- - [ ] Run multi-seed batches under the minimal condition to test winner distribution variance when cross-pairing wins occur.
- - [ ] Enforce whisper constraints via prompt engineering to evaluate whether communication topologies diverge from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261106-1912
python scripts/brief_log.py --print
```
