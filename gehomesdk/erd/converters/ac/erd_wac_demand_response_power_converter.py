from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.ac import *

class ErdWacDemandResponsePowerConverter(ErdReadOnlyConverter[float]):
    def erd_decode(self, value: str) -> float:
        try:
            return float(erd_decode_int(value[:4])) / 1000.0
        except:
            return 0
            
