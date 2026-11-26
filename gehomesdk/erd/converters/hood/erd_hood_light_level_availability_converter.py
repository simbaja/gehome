from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.hood import ErdHoodLightLevelAvailability

class ErdHoodLightLevelAvailabilityConverter(ErdReadOnlyConverter[ErdHoodLightLevelAvailability]):
    def erd_decode(self, value: str) -> ErdHoodLightLevelAvailability:
        try:
            intVal = erd_decode_int(value)
            return ErdHoodLightLevelAvailability(
                intVal & 1 != 0,
                intVal & 2 != 0,
                intVal & 4 != 0,
                intVal & 16 != 0,
                value
            )
        except Exception:
            return ErdHoodLightLevelAvailability(raw_value=value)