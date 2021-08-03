from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.ac import *

class ErdWacDemandResponsePowerConverter(ErdReadOnlyConverter[int]):
    def erd_decode(self, value: str) -> int:
        try:
            return float(erd_decode_int(value[:4])) / 1000.0
        except:
            return 0
            
