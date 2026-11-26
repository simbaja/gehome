from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.ice_maker import ErdUcimCleanStatus

class ErdUcimCleanStatusConverter(ErdReadOnlyConverter[ErdUcimCleanStatus]):
    def erd_decode(self, value: str) -> ErdUcimCleanStatus:
        try:
            return ErdUcimCleanStatus(erd_decode_int(value))
        except Exception:
            return ErdUcimCleanStatus.CLEAN

