from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.advantium import ErdAdvantiumPrecisionMinMax

class ErdAdvantiumPrecisionMinMaxConverter(ErdReadOnlyConverter[ErdAdvantiumPrecisionMinMax]):
    def erd_decode(self, value: str) -> ErdAdvantiumPrecisionMinMax:
        if value == None or value == "" or value == "00000000000000000000": 
            return ErdAdvantiumPrecisionMinMax(
                is_valid = False
            )

        return ErdAdvantiumPrecisionMinMax(
            is_valid=True,
            min_time=erd_decode_timespan(value[0:2], uom="seconds"),
            max_time=erd_decode_timespan(value[4:8], uom="seconds"),
            custom_low_min_time=erd_decode_timespan(value[8:12], uom="seconds"),
            custom_low_max_time=erd_decode_timespan(value[12:16], uom="seconds"),
            custom_high_min_time=erd_decode_timespan(value[16:20], uom="seconds"),
            custom_high_max_time=erd_decode_timespan(value[20:24], uom="seconds"),
            raw_value=value
        )