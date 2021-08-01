from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.wac import *

class ErdWacFilterStatusConverter(ErdReadOnlyConverter[ErdWacFilterStatus]):
    def erd_decode(self, value: str) -> ErdWacFilterStatus:
        try:
            return ErdWacFilterStatus(erd_decode_int(value))
        except:
            return ErdWacFilterStatus.DEFAULT
            
