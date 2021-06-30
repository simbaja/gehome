from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.waterfilter import ErdWaterFilterLeakValidity


class ErdFilterLeakValidityConverter(ErdReadOnlyConverter[ErdWaterFilterLeakValidity]):
    def erd_decode(self, value) -> ErdWaterFilterLeakValidity:
        try:
            return ErdWaterFilterLeakValidity(value)
        except ValueError:
            return ErdWaterFilterLeakValidity.NONE
