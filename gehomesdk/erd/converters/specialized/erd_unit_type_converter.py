from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.common import ErdUnitType

class ErdUnitTypeConverter(ErdReadOnlyConverter[ErdUnitType]):
    def erd_decode(self, value: str) -> ErdUnitType:
        return ErdUnitType(erd_decode_int(value))
