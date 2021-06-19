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
            convection_min_time=erd_decode_timespan_seconds(value[0:4]),
            convection_max_time=erd_decode_timespan_seconds(value[4:8]),
            broil_min_time=erd_decode_timespan_seconds(value[8:12]),
            broil_max_time=erd_decode_timespan_seconds(value[12:16]),
            warm_min_time=erd_decode_timespan_seconds(value[16:20]),
            warm_max_time=erd_decode_timespan_seconds(value[20:24]),
            proof_min_time=erd_decode_timespan_seconds(value[24:28]),
            proof_max_time=erd_decode_timespan_seconds(value[28:32]),
            slow_cook_min_time=erd_decode_timespan_seconds(value[32:36]),
            slow_cook_max_time=erd_decode_timespan_seconds(value[36:40]),

            raw_value=value
        )