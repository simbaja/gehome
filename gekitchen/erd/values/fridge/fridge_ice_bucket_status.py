from typing import NamedTuple
from .erd_full_not_full import ErdFullNotFull

class FridgeIceBucketStatus(NamedTuple):
    state_full_fridge: ErdFullNotFull
    state_full_freezer: ErdFullNotFull
    is_present_fridge: bool
    is_present_freezer: bool
    total_status: ErdFullNotFull
   
