# Run 006: `scheduled/minimal/cron-20260821-1300`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-21 |
| Condition | `minimal` |
| Seed | 2026082113 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260821-1300` |

## Headline arc

- **Day 1:** Initial pairings formed (Maya & Luca, Zara & Kai, Nia & Theo).
- **Day 3:** Bombshell Rio enters, stealing Kai; Zara shifts to Theo, leaving Nia single and dumped.
- **Day 4:** Hideaway dates conducted for Luca & Maya, Theo & Zara, and Kai & Rio.
- **Day 5:** Bombshell Freya enters, stealing Rio; Kai is left single and dumped.
- **Day 6:** Public vote places Rio at risk; Rio is dumped by islander vote.
- **Day 7:** Luca & Maya win the season and £50,000 with a couple score of 147 against Theo & Zara's 143.

## Insights

- **Persistent zero-whisper baseline:** Across 709 events, the run registered 0 whispers, confirming that Gemini Flash Lite relies entirely on public speech channels regardless of prompt variants.
- **Talk vs. couple divergence:** High-frequency talk pairings like Maya & Zara (34) and Kai & Luca (21) reflect broad cross-cutting social engagement rather than romantic alignment.
- **Structural compliance:** Agent thoughts emphasize emotional motivations, but operational behavior maps directly onto forced recoupling windows and bombshell interventions.
- **Pacing inversion:** Unlike prior runs where Day 1 couples dominated to the end, Luca & Maya surged from mid-run stability to secure the win over persistent early pairing Theo & Zara.

## Limits

- Single-run observation ($n=1$) using homogeneous Gemini Flash Lite instances under a specific seed constraint.
- Complete absence of whisper actions limits analysis of tactical coalitions or private secrets.
- Season progression is entirely governed by hard-coded schedule milestones rather than emergent social pacing.

## Next from this run

- - [ ] Run multi-seed replications for the minimal condition to test the stability of Luca & Maya win paths.
- - [ ] Force explicit whisper utilization constraints to test if communication topologies diverge from 100% public broadcast.
- - [ ] Compare network density and partner stability metrics against incentive-condition runs to isolate the impact of prize-emphasis framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260821-1300
python scripts/brief_log.py --print
```
