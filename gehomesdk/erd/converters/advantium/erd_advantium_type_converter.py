from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.advantium import ErdAdvantiumType

class ErdAdvantiumTypeConverter(ErdReadOnlyConverter[ErdAdvantiumType]):
    def erd_decode(self, value: str) -> ErdAdvantiumType:
        return ErdAdvantiumType(erd_decode_int(value))
