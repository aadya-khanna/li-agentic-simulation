# Run 073: `scheduled/minimal/cron-20261107-1741`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-07 |
| Condition | `minimal` |
| Seed | 2026110717 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261107-1741` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 steals agent-4; cascading shifts leave agent-6 dumped while agent-1 pivots to agent-5.
- **Day 5:** Bombshell agent-8 steals agent-5; secondary shifts leave agent-7 dumped and re-pairs agent-1 with agent-4.
- **Day 6:** Safe islanders vote out bombshell agent-8 after a public risk designation.
- **Day 7:** Original Day-1 survival couple agent-2 and agent-3 win the season and £50,000.

## Insights

- **Day-1 survival dominance:** Unlike runs featuring cross-pairing upsets, this iteration demonstrates the triumph of a stable, uninterrupted original couple (agent-2/agent-3).
- **Strict communication constraints:** Replicates a 0.0% whisper rate, enforcing all social interaction through public broadcast networks.
- **Artificially rigid reciprocity:** Contact reciprocity locks completely at 1.0 despite high structural churn and multiple bombshell interventions.
- **Model generation overhead:** Significant token generation friction is evidenced by 96 pass events (16.05% pass rate), highlighting behavioral pacing constraints in the backend model.
- **Top talk pair alignment:** The top talking pair (agent-2 and agent-3 with 18 exchanges) directly correlates with the winning couple.

## Limits

- Single-run observation ($n=1$) bound to a specific random seed and prompt initialization.
- Complete absence of private whisper telemetry limits structural network analysis to public dialog spaces.
- Chronological progression relies on hard-coded environmental triggers rather than endogenous behavioral pacing.

## Next from this run

- - [ ] Run multi-seed batches under the minimal condition to test winner distribution variance when original pairs win.
- - [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies diverge from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261107-1741
python scripts/brief_log.py --print
```
