from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterAlertTimeSettings

class ErdWaterFilterAlertSettingsConverter(ErdReadOnlyConverter[ErdWaterFilterAlertTimeSettings]):
    def erd_decode(self, value: str) -> ErdWaterFilterAlertTimeSettings:
        return ErdWaterFilterAlertTimeSettings(low_alert_time=erd_decode_int(value[0:4]),
                                            medium_alert_time=erd_decode_int(value[4:8]),
                                            high_alert_time=erd_decode_int(value[8:12]))
