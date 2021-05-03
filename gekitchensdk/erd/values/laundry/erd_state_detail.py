import enum
from typing import Optional
from .laundry_const import *

@enum.unique
class ErdLaundryStateDetail(enum.Enum):
    IDLE = 0
    STANDBY = 1
    RUN = 2
    PAUSE = 3
    END_OF_CYCLE = 4
    DSM_DELAY_RUN = 5
    DELAY_RUN = 6
    DELAY_PAUSE = 7
    DRAIN_TIMEOUT = 8
    CLEAN_SPEAK = 128

   def stringify(self, **kwargs) -> Optional[str]:
       from .state_detail_mapping import LAUNDRY_STATE_DETAIL_MAP
       return LAUNDRY_STATE_DETAIL_MAP.get(self, LAUNDRY_STATE_UNKNOWN)
    def __str__(self) -> str:
        return self.stringify() or LAUNDRY_STATE_UNKNOWN

