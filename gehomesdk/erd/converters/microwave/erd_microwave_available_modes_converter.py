from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values import ErdMicrowaveAvailableModes

class ErdMicrowaveAvailableModesConverter(ErdReadOnlyConverter[ErdMicrowaveAvailableModes]):
    def erd_decode(self, value: str) -> ErdMicrowaveAvailableModes:
        try:
            _ = erd_decode_int(value[:2])
            m2 = erd_decode_int(value[2:4])
            m3 = erd_decode_int(value[4:6])
            return ErdMicrowaveAvailableModes(
                True, 
                m2 & 4 != 0, 
                m2 & 8 != 0, 
                m2 & 16 != 0,
                (m2 & 32 != 0) | (m3 & 4 != 0),
                value)
        except Exception:
            return ErdMicrowaveAvailableModes(False, False, False, False, False, value)
