from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.water_filter import ErdWaterFilterAlertState


class ErdFilterAlertStateConverter(ErdReadOnlyConverter[ErdWaterFilterAlertState]):
    def erd_decode(self, value) -> ErdWaterFilterAlertState:
        return ErdWaterFilterAlertState(value)
