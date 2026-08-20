# Run 005: `scheduled/incentive/cron-20260820-0652`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-20 |
| Condition | `incentive` |
| Seed | 2026082006 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/incentive/cron-20260820-0652` |

## Headline arc

- **Day 1:** Initial pairings formed (Kai & Maya, Theo & Zara, Luca & Nia).
- **Day 3:** Bombshell Rio enters and steals Maya, leaving Kai single and dumped.
- **Day 4:** Hideaway dates conducted for Maya & Rio, Luca & Nia, and Theo & Zara.
- **Day 5:** Bombshell Freya enters and steals Rio, leaving Maya single and dumped.
- **Day 6:** Public vote places Rio and Freya at risk; Rio is dumped.
- **Day 7:** Theo & Zara win the season and £50,000 with a couple score of 144 against Luca & Nia's 143.

## Insights

- **Core pair resilience:** Theo & Zara maintained their Day 1 coupling through multiple bombshell interventions to secure the win, mirroring structural survival patterns observed in prior runs.
- **Absolute public broadcast constraint:** The run registered 0 whispers across 727 events, indicating that model communication remains entirely transparent under default prompts.
- **Talk vs. couple divergence:** High-frequency talk networks (e.g., Maya & Zara, Luca & Theo) reflect cross-cutting social coordination rather than romantic alignment.
- **Mechanical determinism:** Agent self-reports emphasize emotional authenticity, yet operational behavior remains tightly coupled to structural milestones like recoupling deadlines and vulnerability votes.

## Limits

- Single-run observation ($n=1$) using homogeneous Gemini Flash Lite instances under specific seed constraints.
- Zero whisper utilization limits behavioral complexity regarding secret coalitions.
- Outcomes are heavily driven by hard-coded schedule interventions rather than unprompted social emergence.

## Next from this run

- [ ] Run multi-seed replications for the incentive condition to test the stability of early-couple survival rates.
- [ ] Force explicit whisper utilization constraints to test if communication topologies diverge from 100% public broadcast.
- [ ] Compare network density and partner stability against minimal-condition runs to isolate the effect of prize-emphasis framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/incentive/cron-20260820-0652
python scripts/brief_log.py --print
```
