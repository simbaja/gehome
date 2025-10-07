import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.advantium import ErdAdvantiumKitchenTimerMinMax

_LOGGER = logging.getLogger(__name__)

class ErdAdvantiumKitchenTimerMinMaxConverter(ErdReadOnlyConverter[ErdAdvantiumKitchenTimerMinMax]):
    def erd_decode(self, value: str) -> ErdAdvantiumKitchenTimerMinMax:
        kitchen_timer_min_max = ErdAdvantiumKitchenTimerMinMax(
            min_time=erd_decode_timespan(value[0:4], uom="seconds"),
            max_time=erd_decode_timespan(value[4:8], uom="seconds"),
            raw_value=value
        )
        _LOGGER.debug("Kitchen Timer for value %s is: %s", value, kitchen_timer_min_max)
        return kitchen_timer_min_max
        
