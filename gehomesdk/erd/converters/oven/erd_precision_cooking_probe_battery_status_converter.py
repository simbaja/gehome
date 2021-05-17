from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import ErdPrecisionCookingProbeBatteryStatus

class ErdPrecisionCookingProbeBatteryStatusConverter(ErdReadOnlyConverter[ErdPrecisionCookingProbeBatteryStatus]):
    def erd_decode(self, value: str) -> ErdPrecisionCookingProbeBatteryStatus:
        if value:
            try:
                return ErdPrecisionCookingProbeBatteryStatus(erd_decode_int(value[:2]))  
            except ValueError:
                return ErdPrecisionCookingProbeBatteryStatus.NA
        else:
            return ErdPrecisionCookingProbeBatteryStatus.NA
        
