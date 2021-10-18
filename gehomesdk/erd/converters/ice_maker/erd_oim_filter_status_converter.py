from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.ice_maker import *

class ErdOimFilterStatusConverter(ErdReadOnlyConverter[ErdOimFilterStatus]):
    def erd_decode(self, value: str) -> ErdOimFilterStatus:
        try:
            return ErdOimFilterStatus(erd_decode_int(value))
        except:
            return ErdOimFilterStatus.EXPIRED

