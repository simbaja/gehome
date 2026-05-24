from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values import ErdCooktopGasValveLockRequest

class ErdCooktopGasValveLockRequestConverter(ErdReadOnlyConverter[ErdCooktopGasValveLockRequest]):
    def erd_decode(self, value) -> ErdCooktopGasValveLockRequest:
        try:
            return ErdCooktopGasValveLockRequest(erd_decode_int(value))
        except ValueError:
            return ErdCooktopGasValveLockRequest.DO_NOTHING

    def erd_encode(self, value: ErdCooktopGasValveLockRequest) -> str:
        return erd_encode_int(value.value)
