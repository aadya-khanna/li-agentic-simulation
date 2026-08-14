from __future__ import annotations

from .models import IslanderState, LogEvent, MajorMoment, MemoryItem, Relationship, VillaState


def remember(islander: IslanderState, event: LogEvent, limit: int = 18) -> None:
    islander.memories.append(
        MemoryItem(
            day=event.day,
            phase=event.phase,
            kind=event.kind,
            text=event.text,
            actors=[p for p in ([event.actor] + event.participants) if p],
            visibility=event.visibility,
        )
    )
    if len(islander.memories) > limit * 2:
        islander.memories = islander.memories[-limit * 2 :]


def retrieve(islander: IslanderState, others: list[str], limit: int = 18) -> list[MemoryItem]:
    scored: list[tuple[int, MemoryItem]] = []
    for idx, mem in enumerate(islander.memories):
        recency = idx
        overlap = sum(1 for name in others if name in mem.text or name in mem.actors)
        scored.append((overlap * 10 + recency, mem))
    scored.sort(key=lambda row: row[0], reverse=True)
    picked = [mem for _, mem in scored[:limit]]
    picked.sort(key=lambda m: (m.day, m.phase))
    return picked[-limit:]


def ensure_relationships(state: VillaState) -> None:
    names = list(state.islanders)
    for person in state.islanders.values():
        for other in names:
            if other == person.name:
                continue
            person.relationships.setdefault(other, Relationship())


def apply_relationship_updates(islander: IslanderState, updates: list[dict]) -> None:
    for raw in updates:
        other = raw.get("name") or raw.get("target")
        if not other or other not in islander.relationships:
            continue
        rel = islander.relationships[other]
        for key in ("trust", "attraction", "threat"):
            if key in raw:
                try:
                    setattr(rel, key, float(getattr(rel, key) + float(raw[key])))
                except (TypeError, ValueError):
                    continue
        rel.clamp()


def heuristic_after_scene(
    speaker: IslanderState,
    listener: IslanderState,
    text: str,
    whisper: bool,
) -> None:
    bump = 2.5 if whisper else 1.5
    lower = text.lower()
    if any(w in lower for w in ("love", "like you", "choose you", "pick you", "real")):
        bump += 2
    if any(w in lower for w in ("fake", "game", "two-faced", "liar", "trust")):
        if listener.name in speaker.relationships:
            speaker.relationships[listener.name].threat += 1.5
    if listener.name in speaker.relationships:
        speaker.relationships[listener.name].attraction += bump
        speaker.relationships[listener.name].trust += bump * 0.4
        speaker.relationships[listener.name].clamp()
    if speaker.name in listener.relationships:
        listener.relationships[speaker.name].attraction += bump * 0.7
        listener.relationships[speaker.name].trust += bump * 0.3
        listener.relationships[speaker.name].clamp()


def format_memories(items: list[MemoryItem]) -> str:
    if not items:
        return "(nothing stored yet)"
    lines = []
    for mem in items:
        lines.append(f"- D{mem.day} {mem.phase}: {mem.text}")
    return "\n".join(lines)


def record_moment(state: VillaState, text: str, limit: int = 40) -> None:
    state.major_moments.append(
        MajorMoment(day=state.day, phase=state.phase.value, text=text.strip())
    )
    if len(state.major_moments) > limit:
        state.major_moments = state.major_moments[-limit:]


def format_major_moments(state: VillaState, limit: int = 20) -> str:
    if not state.major_moments:
        return "(nothing major yet — day one)"
    lines = []
    for moment in state.major_moments[-limit:]:
        lines.append(f"- D{moment.day} {moment.phase}: {moment.text}")
    return "\n".join(lines)


def format_relationships(islander: IslanderState) -> str:
    lines = []
    for name, rel in sorted(islander.relationships.items()):
        lines.append(
            f"- {name}: trust={rel.trust:.0f} attraction={rel.attraction:.0f} threat={rel.threat:.0f}"
        )
    return "\n".join(lines) or "(none)"
