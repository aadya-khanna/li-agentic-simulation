# Run 010: `scheduled/minimal/cron-20260829-1635`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-29 |
| Condition | `minimal` |
| Seed | 2026082916 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260829-1635` |

## Headline arc

- **Day 1:** Initial couplings formed (Maya & Kai, Zara & Theo, Nia & Luca).
- **Day 3:** Bombshell Rio enters, stealing Maya; Nia pivots to Kai, leaving Luca single and dumped.
- **Day 4:** Hideaway dates conducted for Maya & Rio, Theo & Zara, and Kai & Nia.
- **Day 5:** Bombshell Freya enters, stealing Rio; Maya is left single and dumped.
- **Day 6:** Public vote places Rio at risk; Rio is dumped via islander vote.
- **Day 7:** Theo & Zara win the season and £50,000, defeating Kai & Nia.

## Insights

- **Persistent zero-whisper baseline:** Replicates previous minimal runs with 0 whisper actions across 713 events, confirming that Gemini Flash Lite relies entirely on public speech channels.
- **Foundational stability under minimal conditions:** Theo & Zara maintain their Day 1 pairing through the entire run, mirroring successful trajectories seen in other minimal and incentive configurations.
- **High contact density without private subnets:** Achieved a 0.7857 contact density while maintaining zero hidden communication, illustrating broad public social structuring.
- **Divergence in network topologies:** High-frequency dialogue interactions (e.g., Nia & Zara, Kai & Theo) track broad social engagement rather than exclusive romantic pairing stability.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260829-1635
python scripts/brief_log.py --print
```
