from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterLeakDetected


class ErdFilterLeakDetectedConverter(ErdReadOnlyConverter[ErdWaterFilterLeakDetected]):
    def erd_decode(self, value) -> ErdWaterFilterLeakDetected:
        try:
            return ErdWaterFilterLeakDetected(value)
        except ValueError:
            return ErdWaterFilterLeakDetected.NO_LEAK
