from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdSacAvailableModes

class ErdSacAvailableModesConverter(ErdReadOnlyConverter[ErdSacAvailableModes]):
    def erd_decode(self, value: str) -> ErdSacAvailableModes:
        try:
            modes = erd_decode_int(value)
            return ErdSacAvailableModes(modes & 1 == 1, modes & 2 == 2, modes & 4 == 4, value)
        except:
            return ErdSacAvailableModes(False, False, False, value)