from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values import ErdAcAvailableTurboQuietModes

class ErdAcAvailableTurboQuietModesConverter(ErdReadOnlyConverter[ErdAcAvailableTurboQuietModes]):
    def erd_decode(self, value: str) -> ErdAcAvailableTurboQuietModes:
        try:
            modes = erd_decode_int(value)
            return ErdAcAvailableTurboQuietModes(
                modes & 1 == 1, modes & 2 == 2, modes & 4 == 4,
                value)
        except:
            return ErdAcAvailableTurboQuietModes(
                False, False, False,
                value)