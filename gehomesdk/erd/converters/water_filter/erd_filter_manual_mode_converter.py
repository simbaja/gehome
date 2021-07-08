from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterManualMode


class ErdFilterManualModeConverter(ErdReadOnlyConverter[ErdWaterFilterManualMode]):
    def erd_decode(self, value) -> ErdWaterFilterManualMode:
        try:
            return ErdWaterFilterManualMode(value)
        except ValueError:
            return ErdWaterFilterManualMode.NOT_MANUAL
