from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.ac import ErdAcFilterStatus

class ErdAcFilterStatusConverter(ErdReadOnlyConverter[ErdAcFilterStatus]):
    def erd_decode(self, value: str) -> ErdAcFilterStatus:
        try:
            return ErdAcFilterStatus(erd_decode_int(value))
        except Exception:
            return ErdAcFilterStatus.DEFAULT
            
