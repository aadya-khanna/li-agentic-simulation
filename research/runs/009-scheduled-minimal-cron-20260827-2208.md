# Run 009: `scheduled/minimal/cron-20260827-2208`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-27 |
| Condition | `minimal` |
| Seed | 2026082722 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260827-2208` |

## Headline arc

- **Day 1:** Initial pairings formed (Maya & Kai, Zara & Theo, Nia & Luca).
- **Day 3:** Bombshell Rio enters, stealing Nia; Luca is left single and dumped.
- **Day 4:** Hideaway dates conducted for Kai & Maya, Theo & Zara, and Nia & Rio.
- **Day 5:** Bombshell Freya enters, stealing Rio; Nia is left single and dumped.
- **Day 6:** Public vote places Rio at risk; Rio is dumped via islander vote.
- **Day 7:** Theo & Zara win the season and £50,000 with a couple score of 147, defeating Kai & Maya (146).

## Insights

- **Persistent zero-whisper baseline:** Replicates previous runs with 0 whisper actions across 703 events, confirming that Gemini Flash Lite relies entirely on public speech channels.
- **Structural alignment over internal agency:** Agent self-reports emphasize relational continuity, yet final outcomes map directly to hard-coded bombshell schedules and recoupling windows.
- **High contact density without private subnets:** Achieved a 0.75 contact density while maintaining zero hidden communication, illustrating broad public social structuring.
- **Divergence in network topologies:** High-frequency dialogue interactions (e.g., Kai & Theo, Nia & Zara) track broad social engagement rather than exclusive romantic pairing stability.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private strategies.
- Season progression is entirely governed by hard-coded schedule milestones rather than emergent social pacing.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260827-2208
python scripts/brief_log.py --print
```
