from typing import NamedTuple, Optional
from .erd_full_not_full import ErdFullNotFull

class FridgeIceBucketStatus(NamedTuple):
    state_full_fridge: ErdFullNotFull
    state_full_freezer: ErdFullNotFull
    is_present_fridge: bool
    is_present_freezer: bool
    total_status: ErdFullNotFull
   
    def stringify(self, **kwargs) -> Optional[str]:     
        if self.total_status == ErdFullNotFull.FULL:
            return "Full"
        if self.total_status == ErdFullNotFull.NOT_FULL:
            return "Not Full"
        if self.total_status == ErdFullNotFull.NA:
            return "NA"
        return None
    def __str__(self) -> str:
        return self.stringify() or ""