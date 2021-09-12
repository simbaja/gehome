from typing import Set
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import ErdAvailableCookMode, ErdOvenCookMode

class ErdAvailableCookModeConverter(ErdReadOnlyConverter[Set[ErdOvenCookMode]]):
    def erd_decode(self, value: str) -> Set[ErdOvenCookMode]:
        if not value:
            return {ErdAvailableCookMode.OVEN_BAKE.value.cook_mode}
        mode_bytes = [int(i) for i in erd_decode_bytes(value)]
        available_modes = {
            mode.value.cook_mode
            for mode in ErdAvailableCookMode
            if mode_bytes[mode.value.byte] & mode.value.mask
        }
        
#        #Additional fixes for weirdness - guessing the decoding isn't accurate
#        if ErdOvenCookMode.CONVBAKE_DELAYSTART in available_modes:
#            available_modes.add(ErdOvenCookMode.CONVBAKE_NOOPTION)
#        if ErdOvenCookMode.CONVROAST_DELAYSTART in available_modes:
#            available_modes.add(ErdOvenCookMode.CONVROAST_NOOPTION)

        return available_modes
