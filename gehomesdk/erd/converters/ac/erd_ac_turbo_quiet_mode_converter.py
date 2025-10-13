from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from gehomesdk.erd.values.ac import ErdAcTurboQuietMode

class ErdAcTurboQuietModeConverter(ErdReadWriteConverter[ErdAcTurboQuietMode]):
    def erd_decode(self, value: str) -> ErdAcTurboQuietMode:
        try:
            return ErdAcTurboQuietMode(erd_decode_int(value))
        except:
            return ErdAcTurboQuietMode.UNAVAILABLE

    def erd_encode(self, value: ErdAcTurboQuietMode) -> str:
        return erd_encode_int(value.value, 1)
