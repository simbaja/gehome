from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.water_filter import ErdWaterFilterLeakValidity


class ErdFilterLeakValidityConverter(ErdReadOnlyConverter[ErdWaterFilterLeakValidity]):
    def erd_decode(self, value) -> ErdWaterFilterLeakValidity:
        try:
            return ErdWaterFilterLeakValidity(value)
        except ValueError:
            return ErdWaterFilterLeakValidity.NONE
