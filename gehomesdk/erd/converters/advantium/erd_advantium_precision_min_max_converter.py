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
            min_time=erd_decode_int(value[0:2]),
            max_time=erd_decode_int(value[4:8]),
            custom_low_min_time=erd_decode_int(value[8:12]),
            custom_low_max_time=erd_decode_int(value[12:16]),
            custom_high_min_time=erd_decode_int(value[16:20]),
            custom_high_max_time=erd_decode_int(value[20:24]),
            raw_value=value
        )