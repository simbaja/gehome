from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values import ErdWaterHeaterMixingValveAvailableTankCapacities

class ErdWaterHeaterMixingValveAvailableTankCapacitiesConverter(ErdReadOnlyConverter[ErdWaterHeaterMixingValveAvailableTankCapacities]):
    def erd_decode(self, value: str) -> ErdWaterHeaterMixingValveAvailableTankCapacities:
        try:
            modes = erd_decode_int(value)
            return ErdWaterHeaterMixingValveAvailableTankCapacities(
                bool((modes >> 0) & 1),
                bool((modes >> 1) & 1),
                bool((modes >> 2) & 1),
                value
            )
        except:
            return ErdWaterHeaterMixingValveAvailableTankCapacities(False, False, False, value)