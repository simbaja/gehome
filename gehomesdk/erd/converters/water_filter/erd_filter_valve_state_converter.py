from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterValveState


class ErdFilterValveStateConverter(ErdReadOnlyConverter[ErdWaterFilterValveState]):
    def erd_decode(self, value) -> ErdWaterFilterValveState:
        try:
            return ErdWaterFilterValveState(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdWaterFilterValveState.INVALID
