from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values import ErdAcAvailableModes

class ErdAcAvailableModesConverter(ErdReadOnlyConverter[ErdAcAvailableModes]):
    def erd_decode(self, value: str) -> ErdAcAvailableModes:
        try:
            modes = erd_decode_int(value)
            return ErdAcAvailableModes(
                modes & 1 == 1, modes & 2 == 2, modes & 4 == 4, modes & 8 == 8,
                modes & 16 == 16, modes & 32 == 32, modes & 64 == 64, modes & 128 == 128,
                value)
        except:
            return ErdAcAvailableModes(
                False, False, False, False,
                False, False, False, False,
                value)