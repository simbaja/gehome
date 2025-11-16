from ..abstract import ErdReadWriteConverter
from ..primitives import *
from ...values import ErdWaterFilterPosition
from ....exception import GeSetErdNotAllowedError

class ErdFilterPositionConverter(ErdReadWriteConverter[ErdWaterFilterPosition]):
    def erd_decode(self, value) -> ErdWaterFilterPosition:
        try:
            return ErdWaterFilterPosition(erd_decode_int(value))
        except ValueError:
            return ErdWaterFilterPosition.UNKNOWN

    def erd_encode(self, value: ErdWaterFilterPosition) -> str:
        if value == ErdWaterFilterPosition.UNKNOWN:
            raise GeSetErdNotAllowedError(str(self.erd_code), "Cannot set to unknown filter position.")
        return erd_encode_int(value.value, 1)
