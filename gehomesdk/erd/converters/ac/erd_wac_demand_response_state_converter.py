from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.ac import *

class ErdWacDemandResponseStateConverter(ErdReadOnlyConverter[ErdWacDemandResponseState]):
    def erd_decode(self, value: str) -> ErdWacDemandResponseState:
        try:
            return ErdWacDemandResponseState(erd_decode_int(value))
        except:
            return ErdWacDemandResponseState.NOT_AVAILABLE
            
