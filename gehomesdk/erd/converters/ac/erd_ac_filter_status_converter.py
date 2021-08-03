from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.ac import *

class ErdAcFilterStatusConverter(ErdReadOnlyConverter[ErdAcFilterStatus]):
    def erd_decode(self, value: str) -> ErdAcFilterStatus:
        try:
            return ErdAcFilterStatus(erd_decode_int(value))
        except:
            return ErdAcFilterStatus.DEFAULT
            
