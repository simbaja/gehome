from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterAlertState


class ErdFilterAlertStateConverter(ErdReadOnlyConverter[ErdWaterFilterAlertState]):
    def erd_decode(self, value: str) -> ErdWaterFilterAlertState:
        return ErdWaterFilterAlertState(erd_decode_int(value))
