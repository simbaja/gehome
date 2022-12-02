from typing import NamedTuple, Optional

class ErdErrorState (NamedTuple):
    id: int = 0
    active: bool = False
    raw_value: Optional[str] = None
