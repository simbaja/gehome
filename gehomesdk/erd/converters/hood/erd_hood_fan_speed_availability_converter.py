from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.hood import *

class ErdHoodFanSpeedAvailabilityConverter(ErdReadOnlyConverter[ErdHoodFanSpeedAvailability]):
    def erd_decode(self, value: str) -> ErdHoodFanSpeedAvailability:
        try:
            intVal = erd_decode_int(value)
            return ErdHoodFanSpeedAvailability(
                intVal & 1 != 0,
                intVal & 2 != 0,
                intVal & 4 != 0,
                intVal & 8 != 0,
                intVal & 16 != 0,
                value
            )
        except:
            return ErdHoodFanSpeedAvailability(raw_value=value)