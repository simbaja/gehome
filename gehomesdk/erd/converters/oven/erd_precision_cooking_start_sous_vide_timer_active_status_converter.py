from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import ErdPrecisionCookingStartSousVideTimerActiveStatus

class ErdPrecisionCookingStartSousVideTimerActiveStatusConverter(ErdReadOnlyConverter[ErdPrecisionCookingStartSousVideTimerActiveStatus]):
    def erd_decode(self, value: str) -> ErdPrecisionCookingStartSousVideTimerActiveStatus:
        if value:
            try:
                return ErdPrecisionCookingStartSousVideTimerActiveStatus(erd_decode_int(value[:2]))  
            except ValueError:
                return ErdPrecisionCookingStartSousVideTimerActiveStatus.NA
        else:
            return ErdPrecisionCookingStartSousVideTimerActiveStatus.NA
