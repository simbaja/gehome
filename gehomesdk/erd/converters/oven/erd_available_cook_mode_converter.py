from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import ErdAvailableCookMode

class ErdAvailableCookModeConverter(ErdReadOnlyConverter[ErdAvailableCookMode]):
    def erd_decode(self, value: str) -> ErdAvailableCookMode:
        if not value:
            return {ErdAvailableCookMode.OVEN_BAKE.value.cook_mode}
        mode_bytes = [int(i) for i in erd_decode_bytes(value)]
        available_modes = {
            mode.value.cook_mode
            for mode in ErdAvailableCookMode
            if mode_bytes[mode.value.byte] & mode.value.mask
        }
        return available_modes
