from ..abstract import ErdReadWriteConverter
from ..primitives import *
from ...values.hood import *

class ErdHoodLightLevelNewConverter(ErdReadWriteConverter[ErdHoodLightLevelNew]):
    def erd_decode(self, value: str) -> ErdHoodLightLevelNew:
        try:
            return ErdHoodLightLevelNew(erd_decode_int(value))
        except:
            return ErdHoodLightLevelNew.OFF

    def erd_encode(self, value: ErdHoodLightLevelNew) -> str:
        return erd_encode_int(value.value, 1)
