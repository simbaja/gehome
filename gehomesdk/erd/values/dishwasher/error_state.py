from typing import NamedTuple

class ErdErrorState (NamedTuple):
    id: int = 0
    active: bool = False
    raw_value: str | None = None
