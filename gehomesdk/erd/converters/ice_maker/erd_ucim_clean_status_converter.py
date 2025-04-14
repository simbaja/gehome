from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.ice_maker import *

class ErdUcimCleanStatusConverter(ErdReadOnlyConverter[ErdUcimCleanStatus]):
    def erd_decode(self, value: str) -> ErdUcimCleanStatus:
        try:
            return ErdUcimCleanStatus(erd_decode_int(value))
        except:
            return ErdUcimCleanStatus.CLEAN

