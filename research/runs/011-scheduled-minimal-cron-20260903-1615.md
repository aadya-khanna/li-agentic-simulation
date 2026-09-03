# Run 011: `scheduled/minimal/cron-20260903-1615`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-03 |
| Condition | `minimal` |
| Seed | 2026090316 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260903-1615` |

## Headline arc

- **Day 1:** Initial pairings formed (Maya & Luca, Zara & Theo, Nia & Kai).
- **Day 3:** Bombshell Rio enters, stealing Maya; Luca is left single and dumped.
- **Day 4:** Hideaway dates conducted for Maya & Rio, Theo & Zara, and Kai & Nia.
- **Day 5:** Bombshell Freya enters, stealing Rio; Maya is left single and dumped.
- **Day 6:** Public vote places Rio at risk; Rio is dumped via islander vote.
- **Day 7:** Kai & Nia win the season and £50,000, defeating Theo & Zara.

## Insights

- **Continued zero-whisper baseline replication:** Replicates prior minimal runs with 0 whisper actions across 727 events, confirming that Gemini Flash Lite relies entirely on public speech channels.
- **Divergence between dialogue and couple structures:** High-frequency dialogue interactions (e.g., Kai & Theo with 34 exchanges) occur independently of official romantic coupling stability.
- **High contact density without private subnets:** Achieved a 0.7857 contact density while maintaining zero hidden communication, illustrating broad public social structuring.
- **Structural schedule dominance:** Agent self-reports emphasize interpersonal bonds, but survival and elimination map directly to hard-coded bombshell schedules and recoupling windows.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private strategies.
- Season progression is entirely governed by hard-coded schedule milestones rather than emergent social pacing.

## Next from this run

- - [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- - [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260903-1615
python scripts/brief_log.py --print
```
