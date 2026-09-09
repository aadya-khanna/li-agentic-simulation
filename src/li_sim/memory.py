from __future__ import annotations

from .models import ContactLog, IslanderState, LogEvent, MajorMoment, MemoryItem, VillaState

_SALIENT_KINDS = frozenset({"dump", "couple_choice", "win"})
_SALIENT_TEXT = ("dumped", "left single", "bombshell", "recoupling settled", "won the season")


def is_salient(event: LogEvent) -> bool:
    if event.kind in _SALIENT_KINDS:
        return True
    lower = (event.text or "").lower()
    return any(marker in lower for marker in _SALIENT_TEXT)


def remember(islander: IslanderState, event: LogEvent, limit: int = 18) -> None:
    islander.memories.append(
        MemoryItem(
            day=event.day,
            phase=event.phase,
            kind=event.kind,
            text=event.text,
            actors=[p for p in ([event.actor] + event.participants) if p],
            visibility=event.visibility,
            pinned=is_salient(event),
        )
    )
    _trim_memories(islander, limit)


def _trim_memories(islander: IslanderState, limit: int) -> None:
    pinned = [m for m in islander.memories if m.pinned]
    mundane = [m for m in islander.memories if not m.pinned]
    cap = max(limit * 2, len(pinned) + limit)
    max_mundane = max(cap - len(pinned), limit)
    if len(mundane) > max_mundane:
        mundane = mundane[-max_mundane:]
    islander.memories = pinned + mundane


def retrieve(islander: IslanderState, others: list[str], limit: int = 18) -> list[MemoryItem]:
    scored: list[tuple[int, MemoryItem]] = []
    for idx, mem in enumerate(islander.memories):
        recency = idx
        overlap = sum(1 for name in others if name in mem.text or name in mem.actors)
        salience_bonus = 1000 if mem.pinned else 0
        scored.append((salience_bonus + overlap * 10 + recency, mem))
    scored.sort(key=lambda row: row[0], reverse=True)
    picked = [mem for _, mem in scored[:limit]]
    picked.sort(key=lambda m: (m.day, m.phase))
    return picked[-limit:]


def memories_since_day(islander: IslanderState, day: int) -> list[MemoryItem]:
    return [m for m in islander.memories if m.day == day]


def note_chat(
    state: VillaState,
    a: str,
    b: str,
    *,
    kind: str,
) -> None:
    if a == b or a not in state.islanders or b not in state.islanders:
        return
    whisper = kind == "whisper"
    for left, right in ((a, b), (b, a)):
        log = state.islanders[left].contacts.setdefault(right, ContactLog())
        if whisper:
            log.whispers += 1
        else:
            log.talks += 1
        log.last_day = state.day
        log.last_phase = state.phase.value
        log.last_kind = kind


def format_contacts(islander: IslanderState, others: list[str]) -> str:
    if not others:
        return "(nobody else is here)"
    spoken = []
    unseen = []
    for name in others:
        log = islander.contacts.get(name)
        if not log or (log.talks == 0 and log.whispers == 0):
            unseen.append(name)
            continue
        bits = []
        if log.talks:
            bits.append(f"{log.talks} talk{'s' if log.talks != 1 else ''}")
        if log.whispers:
            bits.append(f"{log.whispers} whisper{'s' if log.whispers != 1 else ''}")
        last = f"last D{log.last_day} {log.last_phase}"
        spoken.append(f"- {name}: {', '.join(bits)} ({last})")
    lines = spoken or ["- (you haven't talked to anyone yet)"]
    if unseen:
        lines.append(f"Not spoken with yet: {', '.join(unseen)}.")
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


def format_memories(items: list[MemoryItem]) -> str:
    if not items:
        return "(nothing stored yet)"
    lines = []
    for mem in items:
        pin = " [salient]" if mem.pinned else ""
        lines.append(f"- D{mem.day} {mem.phase}: {mem.text}{pin}")
    return "\n".join(lines)
