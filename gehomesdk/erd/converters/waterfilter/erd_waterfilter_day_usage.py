from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.waterfilter import ErdWaterFilterDayUsage

class ErdWaterFilterUsageConverter(ErdReadOnlyConverter[ErdWaterFilterDayUsage]):
    def erd_decode(self, value: str) -> ErdWaterFilterDayUsage:
        return ErdWaterFilterDayUsage(usage=float(erd_decode_int(value)))

