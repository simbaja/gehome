from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values import ErdCooktopGasValveLockStatus

class ErdCooktopGasValveLockStatusConverter(ErdReadOnlyConverter[ErdCooktopGasValveLockStatus]):
    def erd_decode(self, value) -> ErdCooktopGasValveLockStatus:
        try:
            return ErdCooktopGasValveLockStatus(erd_decode_int(value))
        except ValueError:
            return ErdCooktopGasValveLockStatus.UNKNOWN
