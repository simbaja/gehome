from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.oven import ErdOvenLightLevel

class ErdOvenLightLevelConverter(ErdReadWriteConverter[ErdOvenLightLevel]):
    def erd_decode(self, value: str) -> ErdOvenLightLevel:
        try:
            return ErdOvenLightLevel(erd_decode_int(value))
        except Exception:
            return ErdOvenLightLevel.NOT_AVAILABLE

    def erd_encode(self, value: ErdOvenLightLevel) -> str:
        return erd_encode_int(value.value, 1)
