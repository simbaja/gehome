from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.ice_maker import ErdOimLightLevel

class ErdOimLightLevelConverter(ErdReadWriteConverter[ErdOimLightLevel]):
    def erd_decode(self, value: str) -> ErdOimLightLevel:
        try:
            return ErdOimLightLevel(erd_decode_int(value))
        except Exception:
            return ErdOimLightLevel.OFF

    def erd_encode(self, value: ErdOimLightLevel) -> str:
        return erd_encode_int(value.value, 1)
