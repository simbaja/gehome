from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.wac import *

class ErdWacOperationModeConverter(ErdReadWriteConverter[ErdWacOperationMode]):
    def erd_decode(self, value: str) -> ErdWacOperationMode:
        try:
            return ErdWacOperationMode(erd_decode_int(value))
        except:
            return ErdWacOperationMode.DEFAULT

    def erd_encode(self, value: ErdWacOperationMode) -> str:
        return erd_encode_int(value.value, 1)
