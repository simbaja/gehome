from gehomesdk.exception.ge_set_erd_not_allowed_error import GeSetErdNotAllowedError
from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values.waterfilter import ErdWaterFilterPosition


class ErdFilterPositionConverter(ErdReadWriteConverter[ErdWaterFilterPosition]):
    def erd_decode(self, value) -> ErdWaterFilterPosition:
        try:
            return ErdWaterFilterPosition(erd_decode_int(value))
        except ValueError:
            return ErdWaterFilterPosition.UNKNOWN

    def erd_encode(self, new_position: ErdWaterFilterPosition) -> str:
        if new_position == ErdWaterFilterPosition.UNKNOWN:
            raise GeSetErdNotAllowedError(new_position)
        return erd_encode_int(new_position.value, 1)
