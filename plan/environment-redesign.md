# Environment redesign — planning

Status: **draft / decisions open**
Owner: research thesis
Goal: richer **emergent behaviour** from **instruction-less** agents by redesigning the
environment (the "box"), which is the only lever we have.

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

## Open decisions (to settle before implementation)

1. **Rewards** — hidden+uncertain criteria / visible-but-de-gamed / peer-determined /
   keep current. (Bundles three knobs: locus of power, visibility, individual-vs-couple —
   may want to unbundle.)
2. **Grouping** — what replaces same-gender huddles + pick-order once gender is removed:
   state-driven groups + rank pick-order / random rotating + winner-picks / no segregated
   huddles / keep gender for now.
3. **Schedule** — state-responsive + agent-triggered / denser fixed script / mostly
   agent-driven.
4. **Memory** — add evolving belief tier / expand capacity + better retrieval / just remove
   noise.

## Cross-cutting notes

- These interlock: hidden reward + belief-memory + state-responsive schedule reinforce each
  other.
- Must define "emergent behaviour" for the thesis (narratives/arcs vs measurable strategy
  divergence vs loyalty-vs-betrayal tension) — that choice reprioritizes the levers.
- Respect AGENTS.md invariants (open identity, no relationship maths, private thought,
  shared constitution) and run cost/length (7 days, stub vs real models).
