from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterSoftenerShutoffValveState
from gehomesdk.exception import GeSetErdNotAllowedError

class ErdWaterSoftenerShutoffValveStateConverter(ErdReadWriteConverter[ErdWaterSoftenerShutoffValveState]):
    def erd_decode(self, value) -> ErdWaterSoftenerShutoffValveState:
        try:
            return ErdWaterSoftenerShutoffValveState(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdWaterSoftenerShutoffValveState.UNKNOWN

    def erd_encode(self, new_position: ErdWaterSoftenerShutoffValveState) -> str:
        if new_position in [ErdWaterSoftenerShutoffValveState.UNKNOWN, ErdWaterSoftenerShutoffValveState.TRANSITION]:
            raise GeSetErdNotAllowedError(new_position)
        return erd_encode_int(new_position.value, 1)