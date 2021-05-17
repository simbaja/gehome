from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import OvenConfiguration, ErdOvenConfiguration

class OvenConfigurationConverter(ErdReadOnlyConverter[OvenConfiguration]):
    def erd_decode(self, value: str) -> OvenConfiguration:
        if not value:
            n = 0
        else:
            n = erd_decode_int(value)

        config = OvenConfiguration(
            has_knob=bool(n & ErdOvenConfiguration.HAS_KNOB.value),
            has_warming_drawer=bool(n & ErdOvenConfiguration.HAS_WARMING_DRAWER.value),
            has_light_bar=bool(n & ErdOvenConfiguration.HAS_LIGHT_BAR.value),
            has_lower_oven=bool(n & ErdOvenConfiguration.HAS_LOWER_OVEN.value),
            has_lower_oven_kitchen_timer=bool(n & ErdOvenConfiguration.HAS_LOWER_OVEN_KITCHEN_TIMER.value),
            raw_value=value,
        )
        return config
