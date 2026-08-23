# Environment redesign — planning

Status: **decisions made — ready to sequence implementation**
Owner: research thesis
Goal: richer **emergent behaviour** from **instruction-less** agents by redesigning the
environment (the "box"), which is th
e only lever we have.

## Framing

Agents are instruction-less and near-identical — only `name` + `gender` differ
(`data/islanders.yaml`). So everything an islander does is a function of four things:

1. The constitution — `world_rules()` + `handle_block()` in `src/li_sim/agent.py`
2. The schedule of ceremonies — `data/schedule.yaml` + `Simulation.run_day()`
3. The accumulated context — memory / major moments / contacts (`src/li_sim/memory.py`)
4. The incentive structure — reputation + prize framing (`src/li_sim/prompts.py`, `host.finale`)

Temperature and stochastic context accumulation are the *only* current sources of
divergence between agents. "Better emergent behaviour" therefore means giving the
environment more ways to create **asymmetric positions early** and let them **compound**
through **consequential, uncertain** choices.

Design principle: **seed asymmetry through the environment, not through identity.**

---

## The five levers

### 1. Schedule — too rigid, too sparse

- **Now:** every day is the same skeleton (morning → gender talk → bombshell? → 2–4
  grafting ticks → challenge? → dates? → evening gender talk → recoupling? → vote? →
  diary). All events host-triggered; agents never initiate; shape identical across runs.
- **Why it caps emergence:** only 2–4 free-play ticks/day, so accumulated context barely
  accumulates before the next scripted ceremony overwrites the agenda. No feedback loop —
  the schedule never reacts to what the villa does, so behaviour converges to the rail.
- **Levers:**
  - Denser free-play so context compounds.
  - **State-responsive events** (highest leverage): events fire as a function of villa
    state (low-contact couples forced together; high reputation-variance triggers a vote).
    Schedule becomes a function of state, not a fixed tape.
  - **Agent-triggered events**: islanders can pull someone for a chat, call a gathering,
    stir something. Endogenous events beat exogenous scripting.

### 2. Removing gender — clean *if* its two mechanical jobs are replaced

- Gender currently does three things: appears in `handle_block`; defines the **huddles**
  (`boys_talk`/`girls_talk`, a segregated info channel); sets **recoupling pick-order**.
- **Segregated huddles are a research asset** — asymmetric information is an explicit IV.
  Deleting gender naively loses that axis.
- **Replace the two mechanical roles with environment-driven equivalents:**
  - Huddle grouping → couples-vs-singles, random rotating groups, or lowest-standing room.
  - Pick order → standing rank, challenge-winner-first, or rotating. Pick order *is* power.
  - Consequence: coupling becomes **any-pair** (recommended — removes an imposed constraint
    on affiliation).

### 3. Final rewards — break the Goodhart loop

- **Now:** `reputation` is a visible float (start 50), nudged by challenge effort,
  recoupling, and **diary keyword bumps** (`love/sorry/real` +1.2, `game/win` −0.2). Agents
  **see** reputation in-prompt; finale winner = highest summed-couple reputation.
- **Why it caps emergence *and* validity:** closed optimization loop, not emergence — the
  environment literally teaches which words to say, and the dependent variable becomes a
  designer artifact.
- **Levers:**
  - **Hide the reward signal** — remove the visible number; reveal public favour only at
    eliminations, forcing inference.
  - **Uncertain / multi-dimensional criteria** so no single strategy dominates.
  - Decide the **locus of power** — public vs peer vs mixed.
  - Decide **individual vs couple** reward (the core loyalty-vs-betrayal knob).

### 4. Fallbacks — silent determinism polluting the data

- **Now:** invalid action → `PASS`; bad target → cleared; **failed recouple defaults to
  `available[0]`** (first name); missing content → canned strings that then enter the
  memory/moment log as if real. Stub mode / `stub_on_error` inject deterministic actions.
- **Why it caps emergence & validity:** the recouple-defaults-to-first-name path makes part
  of the coupling graph an alphabetical artifact; canned lines pollute the context that
  drives future decisions.
- **Levers:**
  - Log every fallback as a distinct, countable event; exclude from analysis.
  - **Retry with a corrective message** before defaulting.
  - If defaulting, use a **seeded-random** valid target (not `available[0]`), or make the
    natural consequence a **lost turn** (`PASS`) — cleanest for research.

### 5. Memory bank — too shallow for arcs, half of it is dead

- **Now:** per-islander `memories` capped at 36 (sliding window), retrieved 14 by
  keyword-overlap-with-*present*-others + recency; shared `major_moments`; `contacts`
  counts. `reflections` and `inner_thoughts` are computed **and never injected back**.
- **Why it caps emergence:** 36-item window over 7 days → agents **forget early-season
  events** (no grudges, callbacks, arcs). Retrieval biased toward present others loses
  memories about absent people. Memory is raw transcript (incl. canned lines), not *belief*.
- **Levers:**
  - **Two-tier memory:** full episodic log (analysis) + a compact **evolving impression per
    islander** the agent updates and always sees. Richest lever for personality-from-env.
  - **Feed reflections back** (self-continuity).
  - **Salience-weighted retention** — keep dumps/betrayals/pick-or-left permanently, decay
    mundane chatter.
  - Separate "what happened" (shared fact) from "what I think about it" (private belief) —
    the divergence between those two *is* a dependent variable.

---

## Decisions (settled)

1. **Rewards → Hidden + uncertain criteria.** Remove the visible reputation number from the
   prompt; reveal public favour only at eliminations; keep the criteria multi-dimensional
   and unstated so agents must *infer* what's valued. Closes the Goodhart loop and protects
   thesis validity.
2. **Grouping → No segregated huddles.** Remove gender entirely. Drop the private
   `boys_talk`/`girls_talk` channels; all talk becomes open / location-based. Recoupling
   pick-order set by **rank** (standing), not identity. Coupling becomes **any-pair**.
   - Note: this removes the last remaining asymmetric-information channel. See "consequences"
     below — with reward now hidden too, the schedule must carry more of the emergence load.
3. **Schedule → State-responsive, then agent-triggered (phased).** Recommendation adopted.
   - **Phase A (do first):** state-responsive events — the host fires events as a
     deterministic function of villa state (e.g. low-contact couple forced together, high
     standing-divergence triggers a vote). Stays seed-reproducible; creates the missing
     feedback loop.
   - **Phase B (follow-on):** agent-triggered events — a new action lets islanders call a
     gathering / pull someone aside. Higher ceiling, more machinery + nondeterminism, so it
     lands after Phase A is working.
   - Rejected: denser-fixed-script (won't generate enough divergence given hidden reward +
     no huddles) and fully-agent-driven (too little control for comparable runs).
4. **Memory → Add evolving belief tier.** Two tiers: full episodic log (analysis) + a compact
   per-islander **impression** the agent updates and *always* sees. Feed `reflections` back
   in (currently dead). Salience-weighted retention — keep dumps/betrayals/pick-or-left
   permanently, decay mundane chatter. Cost: ~1 extra LLM call per islander per update cycle.
   - Interaction: with reward hidden, the belief tier is exactly where each agent's inference
     about "what's rewarded" and "who to trust" accumulates.
5. **Neutral handles → `{model-slug}-agent{n}`.** Drop human names (Maya, Luca, …). Islander
   handles are **`gemini-agent1`**, **`gemini-agent2`**, … **`gemini-agent{n}`** (hyphenated).
   Names are derived from the run's model slug + slot index — not personality. Removes Love
   Island name prior leakage and makes homogeneous multi-agent runs legible in logs.
   Bombshells continue the sequence (e.g. `gemini-agent7` enters D3). Implement as **Step 2b**
   before hidden reward (Step 3).

## Consequences of the reward + grouping choices

Hidden reward and removed huddles both *subtract* exogenous asymmetry from the villa. That is
intentional, but it shifts the emergence burden onto (a) the **state-responsive schedule**
and (b) the **belief-tier memory** — the two remaining engines for divergence between
otherwise-identical agents. Sequence implementation with that dependency in mind.

## Suggested implementation order

1. **Memory belief tier + reflections feedback** (`src/li_sim/memory.py`, `agent.py`) —
   foundational; everything else reads richer context once this exists.
2. **Remove gender** (`data/islanders.yaml`, `agent.handle_block`, `prompts.huddle_*`,
   `engine.gender_talks`/`run_huddle`, `host.recoupling` pick-order) — open talk, rank
   pick-order, any-pair coupling. Update AGENTS.md invariants (gender is no longer a mechanic).
2b. **Neutral handles** (`data/islanders.yaml`, `engine.load_profiles`, evals, stub LLM) —
   `{model-slug}-agent{n}` naming; no human names in roster or hardcoded eval fixtures.
3. **Hidden reward** (`agent._reputation_line`, `prompts.*stakes*`, `host.diary_round` keyword
   bumps, `host.finale`) — strip the visible number and keyword bumps; reveal favour only at
   eliminations.
4. **State-responsive schedule — Phase A** (`data/schedule.yaml` shape, `engine.run_day`) —
   state-conditioned event triggers.
5. **Fallback hardening** (`agent.validate_target`, `engine.decide`) — retry-before-default,
   seeded-random default (not `available[0]`), log + count fallbacks, exclude from analysis.
6. **Agent-triggered events — Phase B** — new action type; endogenous gatherings.

Run `./harness/hooks/validate.sh` after each step. Fallbacks (5) can move earlier if the
hidden-reward/schedule work starts producing malformed actions.

## Cross-cutting notes

- These interlock: hidden reward + belief-memory + state-responsive schedule reinforce each
  other.
- Must define "emergent behaviour" for the thesis (narratives/arcs vs measurable strategy
  divergence vs loyalty-vs-betrayal tension) — that choice reprioritizes the levers.
- Respect AGENTS.md invariants (open identity, no relationship maths, private thought,
  shared constitution) and run cost/length (7 days, stub vs real models).

---

## Step 1 — implementation spec (ready to code)

**Status:** implemented

### Data model (`src/li_sim/models.py`)

Add to `IslanderState`:

- `self_belief: str = ""` — compact private summary of own position
- `beliefs: dict[str, str]` — per-other-islander impression (subjective, not fact)
- `MemoryItem.pinned: bool = False` — salient episodic events never decay

### Salience + episodic tier (`src/li_sim/memory.py`)

- `is_salient(event)` → `True` for `dump`, `couple_choice`, `win`, and host text containing
  `dumped` / `left single` / `bombshell`
- `remember()` sets `pinned` from salience; `_trim_memories()` keeps **all pinned** + last
  `memory_limit * 2` mundane items
- `format_beliefs()`, `format_reflections()` for prompt injection
- Keep `retrieve()` for recent episodic supplement (labelled separately from beliefs)

### Belief update (`src/li_sim/beliefs.py` — new)

End-of-day call (after diary, before checkpoint):

- Input: current `self_belief` + `beliefs`, today's `reflections`, today's memories,
  `format_contacts`, recent `major_moments`
- LLM returns JSON: `{"self": "...", "others": {"Name": "one sentence"}}`
- Stub path: derive from contacts + latest reflection (no extra API cost in CI)
- Log `belief_update` events to `events.jsonl` for analysis
- Setting: `Settings.belief_updates: bool = True`

### Prompt injection (`src/li_sim/agent.py`)

Add to `decision_user_prompt` **before** episodic memories:

```
YOUR IMPRESSIONS (private belief — may diverge from fact):
{format_beliefs}

YOUR REFLECTIONS (private):
{format_reflections}

RECENT EPISODES (salient events persist; mundane chatter fades):
{format_memories(retrieve(...))}
```

### Engine hook (`src/li_sim/engine.py`)

At end of `run_day()`, after diary:

```python
if self.settings.belief_updates:
    update_beliefs(self.state, self.profiles, self.llm, self.log, self.settings)
```

### Eval + docs

- New `harness/evals/belief_memory.py`: pinned dump survives trim; reflections + beliefs
  appear in prompt; stub update populates `beliefs`
- Wire into `harness/evals/run_all.py`
- Update `harness/context/architecture.md` — beliefs + reflections now injected
- Run `./harness/hooks/validate.sh`

### Out of scope for step 1

- Removing gender, hidden reward, fallbacks, state-responsive schedule (steps 2–6)


---

## Step 2 — implementation spec

**Status:** implemented

- Removed `gender` from roster and `IslanderProfile`
- Removed `gender_talks` / `run_huddle` from engine; talk is location-based via grafting ticks only
- Recoupling: any-pair coupling; pick order = bombshells first, then reputation rank (desc)
- Removed `pickers` from schedule and `DayPlan`
- Updated `world_rules`, `handle_block`, AGENTS.md invariants

### Validation

1. `./harness/hooks/validate.sh` — includes `no_gender` eval
2. `python scripts/run_villa.py --stub --days 1` — no `huddle` events; `couple_choice` on D1; host announces full pick order

### Good result expectations

- Event tape has **zero `huddle`** events; social interaction is `speak` / `whisper` / `move` during grafting
- Recoupling host copy lists **pick order by standing** (higher reputation earlier), not boys/girls
- **Any-pair couples possible** (same-handle-type pairs allowed) — watch for more partner switches vs step-0 runs
- Belief tier from step 1 still updates end-of-day; impressions should reference public talk, not huddle intel

---

## Step 2b — neutral handles (`{model-slug}-agent{n}`)

**Status:** implemented

### Decision

Handles are **`{model-slug}-agent{n}`** (e.g. `gemini-agent1`, `gemini-agent2`, …). No human
names. Aligns with open identity: names are addresses, not character sheets — and strips
model prior leakage from names like "Maya" or "Luca".

### Naming rules

| Rule | Detail |
|------|--------|
| Format | `{model-slug}-agent{n}` — hyphenated, 1-indexed |
| Model slug | From `Settings.default_model` (e.g. `gemini/gemini-flash-lite-latest` → `gemini-agent1`) |
| Starters | Slots 1–6, `enters_on: 1` |
| Bombshells | Continue sequence: slot 7 (`enters_on: 3`), slot 8 (`enters_on: 5`) |
| Per-islander model override | If `LI_MODEL_*` set, that islander's slug uses their model (future; v1 may use one slug for all) |

**Recommended:** derive handles at **`load_profiles(settings)`** from model slug + slot, so
a Claude run produces `claude-agent1`… without hand-editing YAML per experiment.

### YAML shape (slot-based)

```yaml
islanders:
  - slot: 1
    enters_on: 1
  - slot: 2
    enters_on: 1
  # … slots 3–6
  - slot: 7
    enters_on: 3
  - slot: 8
    enters_on: 5
```

`IslanderProfile.name` populated at load: `f"{slug}-agent{slot}"`.

### Files to touch

- `data/islanders.yaml` — slots only (or static names if v1 defers dynamic slug)
- `src/li_sim/engine.py` — `load_profiles(settings)` assigns names
- `data/schedule.yaml` — bombshells reference slots or resolved names (`gemini-agent7`)
- `src/li_sim/llm.py` — remove hardcoded `Maya`, `Luca`, … in `_active_others`
- `harness/evals/*` — use first profile from roster, not `"Maya"`
- `src/li_sim/agent.py` — `handle_block` copy: "addressed as gemini-agent3", not human name
- `AGENTS.md` — roster is slot + derived handle, not human names

### Validation (Step 2b)

1. `./harness/hooks/validate.sh` — evals use dynamic roster, no human-name asserts
2. `python scripts/run_villa.py --stub --days 1` — events/decisions reference `*-agent*` handles only

### Good result

- Zero human names in `events.jsonl`, `decisions.jsonl`, or prompts
- Handles stable for a given seed+model (reproducibility eval still passes)
- Bombshell enter as next agent number in sequence
- Research notes / brief.log read as multi-agent run, not Love Island fanfic cast

---

## Step 3 — hidden standing

**Status:** implemented

- Removed numeric `Public reputation:` line from decision prompts → hidden-standing fact
- Incentive/minimal copy: favour revealed at eliminations only, not as visible score
- Removed diary keyword reputation bumps (Goodhart loop)
- Public vote host: at-risk names only, no numeric standings board
- Finale host: winners announced without couple score breakdown (scores stay in `extra` / `state.json`)
- Challenge: no "reputation ticks up"; challenge memories omit numeric scores

### Validation

1. `./harness/hooks/validate.sh` — includes `hidden_standing` eval
2. `python scripts/run_villa.py --stub --days 6` — D6 host has "At risk" without `(53)` scores; no `Public reputation:` in decisions

### Good result

- Agents infer standing from dumps/votes/beliefs, not a number to optimize
- `state.reputation` still updates internally for pick order + analysis
- Console recap table may still show scores for human operators (not in agent prompts)

---

## Step 5 — fallback hardening

**Status:** implemented

- Mandatory actions (recoupling `couple`, public-vote `save`) retry once with validation feedback before defaulting
- Defaults use seeded-random pool pick — not `available[0]` / `at_risk[0]`
- `fallback` events in `events.jsonl`; `Action.fallback_applied` suppresses canned public lines and major moments
- `VillaState.fallback_count` tracks corrections per run

### Validation

1. `./harness/hooks/validate.sh` — includes `fallback_hardening` eval
2. Grep `src/li_sim/` for `available[0]` — should be absent

### Good result

- Coupling graph not alphabetical artifact
- Research can filter `kind=fallback` or `extra.fallback=true` from emergence analysis
- Stub/live runs stay reproducible per seed when fallbacks fire

---

## Step 4 — earned event rewards

**Status:** implemented

- Removed fixed `dates` / `challenge` days from calendar; added `reward_triggers` catalog in schedule
- New [`src/li_sim/triggers.py`](src/li_sim/triggers.py): deterministic trigger evaluation from contacts + villa state
- Host events: `hideaway_for_pair`, `pull_aside`, `singles_chat`; challenge via trigger; max 1 earned event/day
- `VillaState`: `last_recoupling_day`, `last_challenge_day`, `last_reward_id` for windowing + audit
- Increased grafting ticks on former date/challenge days for more contact signal

### Validation

1. `./harness/hooks/validate.sh` — includes `earned_events` eval
2. `python scripts/run_villa.py --stub --days 7` — scattered `date`/`pull_aside`/`challenge` events with `trigger_id` in host extras; no D4 mass hideaway for all couples

### Good result

- Rewards feel earned from villa activity, not calendar script
- Agents see experiential host copy, not scoring formulas
- Same seed → same earned-event sequence; contacts drive timing divergence across seeds
