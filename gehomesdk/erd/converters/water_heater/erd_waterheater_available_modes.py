from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdWaterHeaterAvailableModes

class ErdWaterHeaterAvailableModesConverter(ErdReadOnlyConverter[ErdWaterHeaterAvailableModes]):
    def erd_decode(self, value: str) -> ErdWaterHeaterAvailableModes:
        try:
            modes = erd_decode_int(value)
            return ErdWaterHeaterAvailableModes(
                bool((modes >> 0) & 1),
                bool((modes >> 1) & 1),
                bool((modes >> 2) & 1),
                bool((modes >> 3) & 1),
                bool((modes >> 4) & 1),
                value
            )
        except:
            return ErdWaterHeaterAvailableModes(False, False, False, False, False, value)