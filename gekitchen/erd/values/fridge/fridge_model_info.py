from typing import NamedTuple

class FridgeModelInfo(NamedTuple):
    has_fridge: bool
    has_freezer: bool
    has_convertable_drawer: bool
    doors: int
    raw_value: str
