from typing import NamedTuple, Optional
from datetime import timedelta
from ..common import ErdPresent
from .erd_hot_water_status import ErdHotWaterStatus
from .erd_full_not_full import ErdFullNotFull
from .erd_pod_status import ErdPodStatus

class HotWaterStatus(NamedTuple):
    status: ErdHotWaterStatus
    time_until_ready: Optional[timedelta]
    current_temp: Optional[int]
    tank_full: ErdFullNotFull
    brew_module: ErdPresent
    pod_status: ErdPodStatus

    @property
    def faulted(self) -> Optional[bool]:
        if self.status in [ErdHotWaterStatus.FAULT_NEED_CLEARED, ErdHotWaterStatus.FAULT_LOCKED_OUT]:
            return True
        return False
