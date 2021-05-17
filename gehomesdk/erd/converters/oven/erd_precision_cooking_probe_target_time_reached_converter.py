from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import ErdPrecisionCookingProbeTargetTimeReached

class ErdPrecisionCookingProbeTargetTimeReachedConverter(ErdReadOnlyConverter[ErdPrecisionCookingProbeTargetTimeReached]):
    def erd_decode(self, value: str) -> ErdPrecisionCookingProbeTargetTimeReached:
        if value:
            try:
                return ErdPrecisionCookingProbeTargetTimeReached(erd_decode_int(value[:2]))  
            except ValueError:
                return ErdPrecisionCookingProbeTargetTimeReached.NA
        else:
            return ErdPrecisionCookingProbeTargetTimeReached.NA
