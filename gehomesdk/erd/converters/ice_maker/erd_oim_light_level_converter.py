from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.ice_maker import *

class ErdOimLightLevelConverter(ErdReadWriteConverter[ErdOimLightLevel]):
    def erd_decode(self, value: str) -> ErdOimLightLevel:
        try:
            return ErdOimLightLevel(erd_decode_int(value))
        except:
            return ErdOimLightLevel.OFF

    def erd_encode(self, value: ErdOimLightLevel) -> str:
        return erd_encode_int(value.value, 1)
