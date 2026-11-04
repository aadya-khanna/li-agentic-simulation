# Run 070: `scheduled/minimal/cron-20261104-1938`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-04 |
| Condition | `minimal` |
| Seed | 2026110419 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261104-1938` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters and disrupts the villa, stealing agent-6 and forcing agent-5 to pivot to agent-1, while agent-2 is dumped; agent-3/agent-4 remain steadfast.
- **Day 5:** Bombshell agent-8 enters and steals agent-5, leaving agent-1 to pivot to agent-6 while agent-7 is dumped; agent-3/agent-4 hold their pairing.
- **Day 6:** Safe islanders vote to eliminate bombshell agent-8.
- **Day 7:** Unbroken day-1 survival couple agent-3 and agent-4 win the season and £50,000.

## Insights

- **Structural longevity triumph:** Replicating previous minimal runs, an original day-1 pairing (agent-3/agent-4) successfully translates long-term stability into a season victory.
- **Complete private channel collapse:** Maintains an invariant 0.0% whisper rate across 569 events, confirming that minimal prompt conditions force all interactions into public broadcast channels.
- **Rigid network reciprocity:** Contact reciprocity remains artificially locked at 1.0 despite active bombshell steals, partner switches, and islander elimination votes.
- **Invariant token generation friction:** The model backend shows a 17.05% pass rate (97 pass events), consistent with historical technical overhead metrics.

## Limits

- Single-run observation ($n=1$) constrained to a specific random seed and prompt environment.
- Total absence of private whisper logs limits social network analysis strictly to public dialog channels.
- System progression relies on hard-coded chronological milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to measure winner distribution variance.
- [ ] Enforce whisper constraints via prompt engineering to test whether communication topologies diverge from 100% public broadcast.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261104-1938
python scripts/brief_log.py --print
```
