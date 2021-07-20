from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterFlowRate

class ErdWaterFilterFlowConverter(ErdReadOnlyConverter[ErdWaterFilterFlowRate]):
    def erd_decode(self, value: str) -> ErdWaterFilterFlowRate:
        return ErdWaterFilterFlowRate(flow_rate=float(erd_decode_int(value)) / 100)
