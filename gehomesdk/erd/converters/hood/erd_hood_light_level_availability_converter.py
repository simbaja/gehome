from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.hood import *

class ErdHoodLightLevelAvailabilityConverter(ErdReadOnlyConverter[ErdHoodLightLevelAvailability]):
    def erd_decode(self, value: str) -> ErdHoodLightLevelAvailability:
        try:
            intVal = erd_decode_int(value)
            return ErdHoodLightLevelAvailability(
                intVal & 1 != 0,
                intVal & 2 != 0,
                intVal & 4 != 0,
                value
            )
        except:
            return ErdHoodLightLevelAvailability(raw_value=value)