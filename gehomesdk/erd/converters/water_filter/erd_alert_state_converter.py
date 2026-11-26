from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values import ErdWaterFilterAlertState

class ErdFilterAlertStateConverter(ErdReadOnlyConverter[ErdWaterFilterAlertState]):
    def erd_decode(self, value: str) -> ErdWaterFilterAlertState:
        return ErdWaterFilterAlertState(erd_decode_int(value))
