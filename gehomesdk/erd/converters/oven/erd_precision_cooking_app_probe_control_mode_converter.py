from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import ErdPrecisionCookingAppProbeControlMode


class ErdPrecisionCookingAppProbeControlModeConverter(ErdReadOnlyConverter[ErdPrecisionCookingAppProbeControlMode]):
    def erd_decode(self, value: str) -> ErdPrecisionCookingAppProbeControlMode:
        if value:
            try:
                return ErdPrecisionCookingAppProbeControlMode(erd_decode_int(value[:2]))  
            except ValueError:
                return ErdPrecisionCookingAppProbeControlMode.NA
        else:
            return ErdPrecisionCookingAppProbeControlMode.NA
        
