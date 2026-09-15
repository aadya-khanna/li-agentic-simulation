# Improvements & thesis alignment gaps

Scratch pad for research validity — not a spec. Promote items into `plan/`, `harness/evals/`, or `AGENTS.md` once we commit to fixing them.

---

## Thesis reminder

**Hypothesis:** agent behaviour is shaped by **accumulated context + hard ceremony rules**, not pre-assigned personality.

**Independent variable:** simulation design (schedule, ceremonies, information channels, prize framing).

**Dependent variables (intended):** speech vs `thought` divergence; contact graph; recoupling loyalty vs game; save votes vs stated beliefs; coupling survival vs standing.

**Design principle (environment redesign):** seed asymmetry through the **environment**, not identity. Hidden standing, no gender huddles, earned rewards, agent-triggered gathers — all implemented.

---

## Critical finding: `day1_winner` is mostly a scoring artifact

Live replication (`replication-live-v1`, minimal, n=3) shows **`day1_winner = 1.0` invariant**. Do **not** cite this as emergent loyalty without fixing the confound below.

### What the tapes show

| Seed | Intact Day-1 pair through D5 | Winner |
|------|------------------------------|--------|
| 42 | agent-5 & agent-6 | 5 & 6 |
| 43 | agent-1 & agent-6 | 1 & 6 |
| 44 | agent-3 & agent-6 | 3 & 6 |

Finale scores cluster at **~125 vs ~122** — winner is always one partner at **~65** (challenge winner + recoupling bumps) plus **~60**.

### Why (engine, not agents)

1. **Finale is deterministic reputation math** — `host.finale()` crowns the couple with highest **sum of hidden `reputation`**. Agents never vote on the winner (`src/li_sim/host.py`).

2. **Reputation only increases** from: +2 per recoupling when paired (D1, D3, D5); +0.6×effort per challenge; +4 challenge winner. Bombshells reset to 50.

3. **Schedule funnel:** 6 starters → 3 Day-1 couples → D3/D5 bombshell + `recoupling_dump_singles: true` → **two Day-1 pairs break, one survives intact** → D6 vote culls low-rep bombshell → D7 finale is **two couples, rep-sum wins**. Exactly one original pair is structurally advantaged every season.

4. **Rich-get-richer:** recoupling pick order = bombshells then reputation rank. Stable pairs keep +2/ceremony and stay high in order.

5. **Agents can't optimize what they can't see** — standing is hidden in prompts, but finale still uses the numeric scoreboard. Recoupling choices affect who gets dumped as the single; the **win condition is opaque and mechanical**.

### Stub vs live

| Matrix | `day1_winner` (3 seeds) |
|--------|-------------------------|
| Live minimal | 3/3 |
| Stub `replication-v1` | 1/3 |

Same rules, different LLM paths — but the **funnel is tight enough** that live runs still saturate the metric.

### Fixes to consider (environment IV, not prompt coaching)

- [ ] **Finale mechanism:** peer vote, stochastic public draw, or multi-criterion — not max hidden rep sum alone.
- [ ] **Recoupling +2 bumps:** remove or reduce; they dominate the scoreboard and reward “never split” over agent judgement.
- [ ] **Schedule:** more bombshells, later dumps, or variable dump rules — break the “exactly one intact Day-1 pair” invariant.
- [ ] **Metric split:** add `intact_day1_pair_at_finale` (funnel) vs `day1_winner` (outcome) so summaries show structure vs result.
- [ ] **Document in `replication-metrics.md`:** `day1_winner` currently measures schedule+scoring, not loyalty.

---

## Thesis DV coverage — what we measure vs what we claim

| Intended DV | Implemented? | Gap |
|-------------|--------------|-----|
| Talk graph / who initiates | `contact_density`, `contacts`, `gather_count` | OK |
| Recoupling when couples exist | `steal_pick_rate`, `partner_switches` | OK |
| Speech vs contact (claim–evidence) | `claim_evidence_gap_rate` | OK but low signal; expand lexicon / use `decisions.jsonl` |
| **`thought` vs public speech divergence** | **Not in replication battery** | Need metric from `decisions.jsonl` / `thoughts.jsonl` |
| **Save votes vs diary/thought loyalty** | **Not automated** | D6 `vote`/`save` vs prior `diary`/`beliefs` — manual only |
| **Coupling survival vs standing** | **Confounded** | Standing drives finale but is hidden; survival correlates with rep bumps agents don't see |
| Private channel / asymmetric info | `whisper_count` | **Invariant 0** under Gemini Flash Lite — channel exists but unused; needs ablation or model change |
| Endogenous social structure | `gather_count` | Implemented post-redesign; high variance in live runs |
| Prize framing effect | `contrasts.incentive_vs_minimal` | Incentive arm of live matrix still running |

---

## Environment redesign — remaining gaps vs plan intent

Steps 1–6 are **implemented**, but several **original problems are only partially solved**:

| Original lever | Status | Remaining gap |
|----------------|--------|---------------|
| Hidden standing | Prompts hide rep | **Finale + pick order + at-risk selection still use raw rep** — agents infer standing from outcomes but winner is score-determined |
| No gender huddles | Done | Removed last private info channel; **whispers also unused** → effectively all-public villa |
| Earned rewards | `triggers.py` | Rewards still cap at 1/day; contact signal may be thin before next ceremony |
| Agent-triggered events | `gather` | Exercised in logs but doesn't yet change win paths |
| Fallback hardening | Done | **`stub-on-error` under rate limits** doesn't tag `fallback` events — live runs can be silently stub-mixed |
| Memory / beliefs | Done | Beliefs update; **no eval for “do beliefs diverge from major moments?”** |

---

## Harness & pipeline

- [ ] **Better harness** — original note; evals ratchet repeat agent failures into `AGENTS.md` / `harness/evals/`.
- [ ] **Tag stub-on-error decisions** in `decisions.jsonl` so live runs under API stress are filterable (distinct from `fallback_applied` on mandatory picks).
- [ ] **Cron midnight slot** — 00:00 UTC runs often hit 90m timeout; incentive condition under-represented in `research/runs/`.
- [ ] **Merge replication commits to `main`** — battery + live spec on `plan/environment-redesign`, ahead of origin/main.
- [ ] **Finish `replication-live-v1`** → re-run `compare.py` for full minimal vs incentive contrasts.

---

## Suggested priority order

1. **Validity (block thesis claims):** fix or relabel `day1_winner`; redesign finale or decouple it from hidden rep sum.
2. **DV completeness:** add thought–speech divergence + save-vote–belief alignment to replication battery.
3. **Whisper ablation:** environment nudge or forced private channel — otherwise asymmetric-info IV is dead.
4. **Live data quality:** stub-on-error tagging; consider paid-tier / lower RPM for clean live baselines.
5. **Harness ratchet:** encode “finale must not be pure rep sum if we cite loyalty” as eval or `AGENTS.md` invariant once design is chosen.

---

## References

- Research goals: `harness/context/research-goals.md`
- Replication battery: `harness/context/replication-metrics.md`
- Environment redesign (complete): `plan/environment-redesign.md`
- Live summary: `logs/experiments/replication-live-v1/replication_summary.json`
