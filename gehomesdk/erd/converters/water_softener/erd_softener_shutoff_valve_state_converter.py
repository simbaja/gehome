from ..abstract import ErdReadWriteConverter
from ..primitives import *
from ...values import ErdWaterSoftenerShutoffValveState
from ....exception import GeSetErdNotAllowedError

class ErdWaterSoftenerShutoffValveStateConverter(ErdReadWriteConverter[ErdWaterSoftenerShutoffValveState]):
    def erd_decode(self, value) -> ErdWaterSoftenerShutoffValveState:
        try:
            return ErdWaterSoftenerShutoffValveState(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdWaterSoftenerShutoffValveState.UNKNOWN

    def erd_encode(self, value: ErdWaterSoftenerShutoffValveState) -> str:
        if value in [ErdWaterSoftenerShutoffValveState.UNKNOWN, ErdWaterSoftenerShutoffValveState.TRANSITION]:
            raise GeSetErdNotAllowedError(str(self.erd_code), "Cannot change position while transitioning or in an unknown state.")
        return erd_encode_int(value.value, 1)