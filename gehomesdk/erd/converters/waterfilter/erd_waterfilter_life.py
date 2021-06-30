from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.waterfilter import ErdWaterFilterLifeRemaining


class ErdWaterFilterLifeRemainingConverter(
    ErdReadOnlyConverter[ErdWaterFilterLifeRemaining]
):
    def erd_decode(self, value: str) -> ErdWaterFilterLifeRemaining:
        # TODO:what are value[8:24]?
        return ErdWaterFilterLifeRemaining(
            life_remaining=float(erd_decode_int(value[0:8]))
        )
