from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.coffee_maker import ErdCcmBrewStrength

class ErdCcmBrewStrengthConverter(ErdReadOnlyConverter[ErdCcmBrewStrength]):
    def erd_decode(self, value: str) -> ErdCcmBrewStrength:
        try:
            return ErdCcmBrewStrength(erd_decode_int(value))
        except Exception:
            return ErdCcmBrewStrength.UNKNOWN

