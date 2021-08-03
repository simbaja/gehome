from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.ac import *

class ErdAcOperationModeConverter(ErdReadWriteConverter[ErdAcOperationMode]):
    def erd_decode(self, value: str) -> ErdAcOperationMode:
        try:
            return ErdAcOperationMode(erd_decode_int(value))
        except:
            return ErdAcOperationMode.DEFAULT

    def erd_encode(self, value: ErdAcOperationMode) -> str:
        return erd_encode_int(value.value, 1)
