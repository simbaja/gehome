from typing import NamedTuple, Optional

class ErdCycleCount (NamedTuple):
    started: int = 0
    completed: int = 0
    reset: int = 0
    raw_value: Optional[str] = None
