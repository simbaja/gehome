from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import *

class ErdOvenLightLevelAvailabilityConverter(ErdReadOnlyConverter[ErdOvenLightLevelAvailability]):
    def erd_decode(self, value: str) -> ErdOvenLightLevelAvailability:
        try:
            intVal = erd_decode_int(value[:2])
            return ErdOvenLightLevelAvailability(
                intVal & 4 != 0,
                intVal & 2 != 0,
                intVal & 8 != 0,
                intVal & 1 != 0,
                False,
                value
            )
        except:
            return ErdOvenLightLevelAvailability(raw_value=value)