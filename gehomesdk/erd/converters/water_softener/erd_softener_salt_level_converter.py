from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterSoftenerSaltLevel


class ErdWaterSoftenerSaltLevelConverter(ErdReadOnlyConverter[ErdWaterSoftenerSaltLevel]):
    def erd_decode(self, value) -> ErdWaterSoftenerSaltLevel:
        try:
            return ErdWaterSoftenerSaltLevel(value)
        except ValueError:
            return ErdWaterSoftenerSaltLevel.OK
