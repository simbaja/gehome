from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterMode


class ErdFilterModeConverter(ErdReadOnlyConverter[ErdWaterFilterMode]):
    def erd_decode(self, value) -> ErdWaterFilterMode:
        try:
            return ErdWaterFilterMode(erd_decode_int(value))
        except ValueError:
            return ErdWaterFilterMode.UNKNOWN
