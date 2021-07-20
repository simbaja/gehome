from datetime import timedelta
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterFilterLifeRemaining

class ErdWaterFilterLifeRemainingConverter(
    ErdReadOnlyConverter[ErdWaterFilterLifeRemaining]
):
    def erd_decode(self, value: str) -> ErdWaterFilterLifeRemaining:
        # TODO:what are value[8:24]?
        # From the comfort app, it looks like it's breaking it into two
        # parts, each 8 characters.  It looks like a max lifetime and used
        # lifetime, but the math doesn't work right
        try:
            pct = erd_decode_int(value[0:8])
            return ErdWaterFilterLifeRemaining(
                life_remaining=pct
            )            
        except:
            return ErdWaterFilterLifeRemaining()

