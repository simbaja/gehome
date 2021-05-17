from typing import NamedTuple

class FridgeSetPointLimits(NamedTuple):
    fridge_min: int
    fridge_max: int
    freezer_min: int
    freezer_max: int