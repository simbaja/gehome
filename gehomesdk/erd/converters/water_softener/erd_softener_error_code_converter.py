from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values import ErdWaterSoftenerErrorCode

class ErdWaterSoftenerErrorCodeConverter(ErdReadOnlyConverter[ErdWaterSoftenerErrorCode]):
    def erd_decode(self, value) -> ErdWaterSoftenerErrorCode:
        try:
            return ErdWaterSoftenerErrorCode(erd_decode_int(value))
        except ValueError:
            return ErdWaterSoftenerErrorCode.UNKNOWN
