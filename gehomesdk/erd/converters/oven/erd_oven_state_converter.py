from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import ErdOvenState


class ErdOvenStateConverter(ErdReadOnlyConverter[ErdOvenState]):
    def erd_decode(self, value: str) -> ErdOvenState:
        """
        See erdCurrentState.smali
        """
        state_code = erd_decode_int(value)
        if 44 <= state_code <= 59:
            return ErdOvenState.OVEN_STATE_SPECIAL_X
        if 42 <= state_code <= 43:
            return ErdOvenState.OVEN_STATE_BAKED_GOODS
        if 40 <= state_code <= 41:
            return ErdOvenState.OVEN_STATE_FROZEN_PIZZA_MULTI
        if 38 <= state_code <= 39:
            return ErdOvenState.OVEN_STATE_FROZEN_SNACKS_MULTI
        if 36 <= state_code <= 37:
            return ErdOvenState.OVEN_STATE_FROZEN_PIZZA
        if 33 <= state_code <= 35:
            return ErdOvenState.OVEN_STATE_FROZEN_SNACKS
        if 90 <= state_code <= 91:
            return ErdOvenState.OVEN_STATE_AIRFRY
        if 1 <= state_code <= 27:
            # These 27 were nicely enumerated in v1.0.3 of the app, though the display logic is more similar to
            # to those above, grouping similar things. See ErdCurrentState.smali for more details.
            return ErdOvenState(state_code)
        return ErdOvenState.STATUS_DASH
