from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.ice_maker import *

class ErdOimStatusConverter(ErdReadOnlyConverter[ErdOimStatus]):
    def erd_decode(self, value: str) -> ErdOimStatus:
        try:
            return ErdOimStatus(erd_decode_int(value))
        except:
            return ErdOimStatus.UNKNOWN

