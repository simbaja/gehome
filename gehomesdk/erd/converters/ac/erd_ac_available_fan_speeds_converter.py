from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int

from gehomesdk.erd.values import ErdAcAvailableFanSpeeds

class ErdAcAvailableFanSpeedsConverter(ErdReadOnlyConverter[ErdAcAvailableFanSpeeds]):
    def erd_decode(self, value: str) -> ErdAcAvailableFanSpeeds:
        try:
            modes = erd_decode_int(value)
            return ErdAcAvailableFanSpeeds(
                modes & 1 == 1, modes & 2 == 2, modes & 4 == 4,
                modes & 8 == 8, modes & 16 == 16, modes & 32 == 32,
                value)
        except:
            return ErdAcAvailableFanSpeeds(
                False, False, False,
                False, False, False,
                value)