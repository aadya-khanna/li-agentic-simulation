from __future__ import annotations

import random
import zlib


def derive_seed(base: int, *parts: str | int) -> int:
    blob = "|".join(str(p) for p in (base, *parts))
    return zlib.adler32(blob.encode()) & 0x7FFFFFFF


def seeded_rng(base: int, *parts: str | int) -> random.Random:
    return random.Random(derive_seed(base, *parts))
