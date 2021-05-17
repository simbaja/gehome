from datetime import timedelta

from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.common import ErdPresent
from gehomesdk.erd.values.fridge import HotWaterStatus, ErdHotWaterStatus, ErdFullNotFull, ErdPodStatus

class HotWaterStatusConverter(ErdReadOnlyConverter[HotWaterStatus]):
    def erd_decode(self, value: str) -> HotWaterStatus:
        if not value:
            return HotWaterStatus(
                status=ErdHotWaterStatus.NA,
                time_until_ready=None,
                current_temp=None,
                tank_full=ErdFullNotFull.NA,
                brew_module=ErdPresent.NA,
                pod_status=ErdPodStatus.NA,
            )
        try:
            status = ErdHotWaterStatus(value[:2])
        except ValueError:
            status = ErdHotWaterStatus.NA

        time_until_ready = timedelta(minutes=erd_decode_int(value[2:6]))
        current_temp = erd_decode_int(value[6:8])

        try:
            tank_full = ErdFullNotFull(value[8:10])
        except ValueError:
            tank_full = ErdFullNotFull.NA

        try:
            brew_module = ErdPresent(value[10:12])
        except ValueError:
            brew_module = ErdPresent.NA

        try:
            pod_status = ErdPodStatus(value[12:14])
        except ValueError:
            pod_status = ErdPodStatus.NA

        return HotWaterStatus(
            status=status,
            time_until_ready=time_until_ready,
            current_temp=current_temp,
            tank_full=tank_full,
            brew_module=brew_module,
            pod_status=pod_status,
        )
