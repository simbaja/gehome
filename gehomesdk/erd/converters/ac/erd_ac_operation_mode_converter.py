from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.ac import ErdAcOperationMode

class ErdAcOperationModeConverter(ErdReadWriteConverter[ErdAcOperationMode]):
    def erd_decode(self, value: str) -> ErdAcOperationMode:
        try:
            return ErdAcOperationMode(erd_decode_int(value))
        except Exception:
            return ErdAcOperationMode.DEFAULT

    def erd_encode(self, value: ErdAcOperationMode) -> str:
        return erd_encode_int(value.value, 1)
