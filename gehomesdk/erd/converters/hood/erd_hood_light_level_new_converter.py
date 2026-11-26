from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.hood import ErdHoodLightLevelNew

class ErdHoodLightLevelNewConverter(ErdReadWriteConverter[ErdHoodLightLevelNew]):
    def erd_decode(self, value: str) -> ErdHoodLightLevelNew:
        try:
            return ErdHoodLightLevelNew(erd_decode_int(value))
        except Exception:
            return ErdHoodLightLevelNew.OFF

    def erd_encode(self, value: ErdHoodLightLevelNew) -> str:
        return erd_encode_int(value.value, 1)
