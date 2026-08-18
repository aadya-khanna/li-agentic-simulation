# Run NNN: `<experiment_id>/<condition>/<run_id>`

**Requirement:** full 7-day season (`--days 7`).

## Config

| Field | Value |
|-------|-------|
| Date | YYYY-MM-DD |
| Condition | minimal / incentive |
| Seed | |
| Days | 7 |
| Mode | stub / live |
| Model(s) | |
| Log dir | `logs/experiments/...` |

## Headline arc

(Bullet summary from `brief.log` or manual read)

## Insights

What this run tells us about environment-led behavior, model priors, or apparatus bugs. Be explicit about **n=1** limits.

- 

## Limits

- 

## Next from this run

- [ ] 

## Artifacts

```bash
python viewer/app.py --run-dir experiments/<experiment_id>/<condition>/<run_id>
python scripts/brief_log.py --print
```
