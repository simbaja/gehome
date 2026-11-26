from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.ice_maker import ErdOimStatus

class ErdOimStatusConverter(ErdReadOnlyConverter[ErdOimStatus]):
    def erd_decode(self, value: str) -> ErdOimStatus:
        try:
            return ErdOimStatus(erd_decode_int(value))
        except Exception:
            return ErdOimStatus.UNKNOWN

