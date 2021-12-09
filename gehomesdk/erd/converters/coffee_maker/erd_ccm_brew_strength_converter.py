from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.coffee_maker import *

class ErdCcmBrewStrengthConverter(ErdReadOnlyConverter[ErdCcmBrewStrength]):
    def erd_decode(self, value: str) -> ErdCcmBrewStrength:
        try:
            return ErdCcmBrewStrength(erd_decode_int(value))
        except:
            return ErdCcmBrewStrength.UNKNOWN

