from typing import Set
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.oven import ErdExtendedCookMode, ErdOvenCookMode

class ErdExtendedCookModeConverter(ErdReadOnlyConverter[Set[ErdOvenCookMode]]):
    def erd_decode(self, value: str) -> Set[ErdOvenCookMode]:
        if not value:
            return set[ErdOvenCookMode]()
        mode_bytes = [int(i) for i in erd_decode_bytes(value)]
        available_modes = {
            mode.value.cook_mode
            for mode in ErdExtendedCookMode
            if mode_bytes[mode.value.byte] & mode.value.mask
        }
        return available_modes
