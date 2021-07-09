from datetime import timedelta
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterLifeRemaining

class ErdWaterFilterLifeRemainingConverter(
    ErdReadOnlyConverter[ErdWaterFilterLifeRemaining]
):
    def erd_decode(self, value: str) -> ErdWaterFilterLifeRemaining:
        # TODO:what are value[8:24]?
        # It looks like this is a bigint in the SmartHQ application... maybe nothing else needed here?
        # Left it as a named tuple in case we need to do more.
        try:
            seconds = erd_decode_int(value[0:8])
            return ErdWaterFilterLifeRemaining(
                life_remaining=timedelta(seconds=seconds)
            )            
        except:
            return ErdWaterFilterLifeRemaining()

