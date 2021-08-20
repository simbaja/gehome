import enum
from typing import Optional

from .const import *

@enum.unique
class ErdOvenState(enum.Enum):
    """
    Oven state constants for display purposes.
    These are found in ErdCurrentState.smali.  That they are not aligned with the values for
    ErdCookMode and AvailableCookMode is infuriating.
    """
    BAKE = 5
    BAKE_PREHEAT = 1
    BAKE_TWO_TEMP = 6
    BROIL_HIGH = 14
    BROIL_LOW = 13
    CLEAN_COOL_DOWN = 23
    CLEAN_STAGE1 = 21
    CLEAN_STAGE2 = 22
    CONV_BAKE = 7
    CONV_BAKE_PREHEAT = 2
    CONV_BAKE_TWO_TEMP = 8
    CONV_BROIL_CRISP = 17
    CONV_BROIL_HIGH = 15
    CONV_BROIL_LOW = 16
    CONV_MULTI_BAKE_PREHEAT = 3
    CONV_MULTI_TWO_BAKE = 10
    CONV_MUTLI_BAKE = 9
    CONV_ROAST = 11
    CONV_ROAST2 = 12
    CONV_ROAST_BAKE_PREHEAT = 4
    CUSTOM_CLEAN_STAGE2 = 24
    DELAY = 27
    NO_MODE = 0
    PROOF = 19
    SABBATH = 20
    STEAM_CLEAN_STAGE2 = 25
    STEAM_COOL_DOWN = 26
    WARM = 18
    OVEN_STATE_BAKE = "oven_bake"
    OVEN_STATE_BAKED_GOODS = "oven_state_baked_goods"
    OVEN_STATE_BROIL = "oven_state_broil"
    OVEN_STATE_CONV_BAKE = "oven_state_conv_bake"
    OVEN_STATE_CONV_BAKE_MULTI = "oven_state_conv_bake_multi"
    OVEN_STATE_CONV_BROIL = "oven_state_conv_broil"
    OVEN_STATE_CONV_ROAST = "oven_state_conv_roast"
    OVEN_STATE_DELAY_START = "oven_state_delay_start"
    OVEN_STATE_DUAL_BROIL_HIGH = "oven_state_dual_broil_high"
    OVEN_STATE_DUAL_BROIL_LOW = "oven_state_dual_broil_low"
    OVEN_STATE_FROZEN_PIZZA = "oven_state_frozen_pizza"
    OVEN_STATE_FROZEN_PIZZA_MULTI = "oven_state_frozen_pizza_multi"
    OVEN_STATE_FROZEN_SNACKS = "oven_state_frozen_snacks"
    OVEN_STATE_FROZEN_SNACKS_MULTI = "oven_state_frozen_snacks_multi"
    OVEN_STATE_PROOF = "oven_state_proof"
    OVEN_STATE_SELF_CLEAN = "oven_state_self_clean"
    OVEN_STATE_SPECIAL_X = "oven_state_speical_x"  # [sic.]
    OVEN_STATE_STEAM_START = "oven_state_steam_start"
    OVEN_STATE_WARM = "oven_state_warm"
    OVEN_STATE_AIRFRY = "oven_state_airfry"
    STATUS_DASH = "status_dash"

    def stringify(self, **kwargs) -> Optional[str]:
        from .oven_display_state_mapping import OVEN_DISPLAY_STATE_MAP
        return OVEN_DISPLAY_STATE_MAP.get(self, STATE_OVEN_UNKNOWN)
    def __str__(self) -> str:
        return self.stringify() or STATE_OVEN_UNKNOWN        