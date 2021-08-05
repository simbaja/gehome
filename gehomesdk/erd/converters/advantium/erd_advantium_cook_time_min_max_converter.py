from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.advantium import ErdAdvantiumCookTimeMinMax

class ErdAdvantiumCookTimeMinMaxConverter(ErdReadOnlyConverter[ErdAdvantiumCookTimeMinMax]):
    def erd_decode(self, value: str) -> ErdAdvantiumCookTimeMinMax:
        if value == None or value == "" or value == "00000000000000000000000000000000000000000000000000000000000000000000000000000000": 
            return ErdAdvantiumCookTimeMinMax(
                is_valid = False
            )

        return ErdAdvantiumCookTimeMinMax(
            is_valid=True,
            convection_min_time=erd_decode_timespan(value[0:4], uom="seconds"),
            convection_max_time=erd_decode_timespan(value[4:8], uom="seconds"),
            broil_min_time=erd_decode_timespan(value[8:12], uom="seconds"),
            broil_max_time=erd_decode_timespan(value[12:16], uom="seconds"),
            warm_min_time=erd_decode_timespan(value[16:20], uom="seconds"),
            warm_max_time=erd_decode_timespan(value[20:24], uom="seconds"),
            proof_min_time=erd_decode_timespan(value[24:28], uom="seconds"),
            proof_max_time=erd_decode_timespan(value[28:32], uom="seconds"),
            slow_cook_min_time=erd_decode_timespan(value[32:36], uom="seconds"),
            slow_cook_max_time=erd_decode_timespan(value[36:40], uom="seconds"),

            raw_value=value
        )