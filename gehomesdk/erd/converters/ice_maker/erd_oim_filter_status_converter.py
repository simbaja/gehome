from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.ice_maker import ErdOimFilterStatus

class ErdOimFilterStatusConverter(ErdReadOnlyConverter[ErdOimFilterStatus]):
    def erd_decode(self, value: str) -> ErdOimFilterStatus:
        try:
            return ErdOimFilterStatus(erd_decode_int(value))
        except Exception:
            return ErdOimFilterStatus.EXPIRED

