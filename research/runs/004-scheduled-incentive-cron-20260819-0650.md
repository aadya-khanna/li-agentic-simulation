# Run 004: `scheduled/incentive/cron-20260819-0650`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-19 |
| Condition | `incentive` |
| Seed | 2026081906 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/incentive/cron-20260819-0650` |

## Headline arc

- **Day 1:** Initial pairings formed (Kai & Maya, Theo & Zara, Luca & Nia).
- **Day 3:** Bombshell Rio enters and steals Nia, leaving Luca single and dumped.
- **Day 4:** Hideaway dates conducted for established couples.
- **Day 5:** Bombshell Freya enters and steals Rio, leaving Nia single and dumped.
- **Day 6:** Public vote places Freya and Rio at risk; Freya is dumped.
- **Day 7:** Theo & Zara win the season and £50,000 with a couple score of 148.

## Insights

- **Persistent core survival:** Theo & Zara maintained their pairing from Day 1 through Day 7, successfully insulating themselves against multiple bombshell intrusions to win the run.
- **Complete absence of private channels:** Agents recorded 0 whispers across 723 events, mirroring the previous run's total reliance on public speech and structured actions.
- **Cross-cutting communication:** The highest frequency talk pair was Rio & Theo (21), despite being in separate couples for major portions of the simulation, indicating cross-cleavage social maintenance.
- **Tactical vs narrative alignment:** Agent thought logs consistently frame choices through emotional connection, yet behavior remains tightly bound to structural recoupling deadlines and survival math.

## Limits

- Single-run observation ($n=1$) utilizing homogeneous Gemini Flash Lite instances under specific seed conditions.
- Absence of whisper actions (0.0 whisper rate) restricts behavioral complexity regarding secret alliances.
- Results reflect a hard-coded set of intervention schedules (bombshells, hideaways, votes) rather than emergent pacing.

## Next from this run

- [ ] Execute multi-seed replication for the incentive condition to test the stability of early-couple persistence.
- [ ] Force explicit whisper utilization constraints to test if communication topologies diverge from 100% public broadcast.
- [ ] Compare network density and partner stability against minimal-condition runs to isolate the effect of prize-emphasis framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/incentive/cron-20260819-0650
python scripts/brief_log.py --print
```
