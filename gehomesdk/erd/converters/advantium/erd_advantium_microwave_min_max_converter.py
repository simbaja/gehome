import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.advantium import ErdAdvantiumMicrowaveMinMax

_LOGGER = logging.getLogger(__name__)

class ErdAdvantiumMicrowaveMinMaxConverter(ErdReadOnlyConverter[ErdAdvantiumMicrowaveMinMax]):
    def erd_decode(self, value: str) -> ErdAdvantiumMicrowaveMinMax:
        if value == None or value == "" or value == "00000000000000000000": 
            return ErdAdvantiumMicrowaveMinMax(
                is_valid = False
            )

        microwave_min_max = ErdAdvantiumMicrowaveMinMax(
            is_valid=True,
            min_time=erd_decode_timespan(value[0:4], uom="seconds"),
            max_time=erd_decode_timespan(value[4:8], uom="seconds"),
            slow_cook_min_time=erd_decode_timespan(value[8:12], uom="seconds"),
            slow_cook_max_time=erd_decode_timespan(value[12:16], uom="seconds"),
            raw_value=value
        )
        _LOGGER.debug("Microwave min max for value %s is: %s", value, microwave_min_max)
        return microwave_min_max
