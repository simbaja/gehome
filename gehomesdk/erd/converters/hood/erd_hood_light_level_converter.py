from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.hood import *

class ErdHoodLightLevelConverter(ErdReadWriteConverter[ErdHoodLightLevel]):
    def erd_decode(self, value: str) -> ErdHoodLightLevel:
        try:
            return ErdHoodLightLevel(erd_decode_int(value))
        except:
            return ErdHoodLightLevel.OFF

    def erd_encode(self, value: ErdHoodLightLevel) -> str:
        return erd_encode_int(value.value, 1)
