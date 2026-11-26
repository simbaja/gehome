from typing import NamedTuple

class ErdCycleCount (NamedTuple):
    started: int = 0
    completed: int = 0
    reset: int = 0
    raw_value: str | None = None
