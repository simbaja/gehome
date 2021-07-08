from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterLeakValidity


class ErdFilterLeakValidityConverter(ErdReadOnlyConverter[ErdWaterFilterLeakValidity]):
    def erd_decode(self, value) -> ErdWaterFilterLeakValidity:
        try:
            return ErdWaterFilterLeakValidity(value)
        except ValueError:
            return ErdWaterFilterLeakValidity.NO_LEAK
