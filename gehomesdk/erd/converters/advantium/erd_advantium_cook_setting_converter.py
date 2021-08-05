import logging
from typing import List
from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values.advantium import ErdAdvantiumCookSetting
from gehomesdk.erd.values.advantium.advantium_enums import *

_LOGGER = logging.getLogger(__name__)

class ErdAdvantiumCookSettingConverter(ErdReadWriteConverter[ErdAdvantiumCookSetting]):
    def erd_decode(self, value: str) -> ErdAdvantiumCookSetting:
        if not value:
            return ErdAdvantiumCookSetting()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))
            
            return ErdAdvantiumCookSetting(
                d=int_values[0],
                cook_action = CookAction(int_values[1]),
                cook_mode = CookMode(int_values[2]),
                target_temperature=erd_decode_int(values[3] + values[4]),
                h=int_values[5],
                i=int_values[6],
                power_level=int_values[7],
                k=int_values[8],
                cook_time_remaining=erd_decode_timespan(values[9] + values[10], uom = "seconds"),
                m=int_values[11],
                n=int_values[12],
                o=int_values[13],
                p=int_values[14],
                q=int_values[15],
                r=int_values[16],
                s=int_values[17],
                warm_status = WarmStatus(int_values[18]),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct cook setting, using default.")
            return ErdAdvantiumCookSetting(raw_value=value)
    def erd_encode(self, value: ErdAdvantiumCookSetting) -> str:
        valList: List[str] = [
            erd_encode_int(value.d, 1),
            erd_encode_int(value.cook_action, 1),
            erd_encode_int(value.cook_mode, 1),
            erd_encode_int(value.target_temperature),
            erd_encode_int(value.h, 1),
            erd_encode_int(value.i, 1),
            erd_encode_int(value.power_level, 1),
            erd_encode_int(value.k, 1),
            erd_encode_timespan(value.cook_time_remaining, uom="seconds"),
            erd_encode_int(value.m, 1),
            erd_encode_int(value.n, 1),
            erd_encode_int(value.o, 1),
            erd_encode_int(value.p, 1),
            erd_encode_int(value.q, 1),
            erd_encode_int(value.r, 1),
            erd_encode_int(value.s, 1),
            erd_encode_int(value.warm_status, 1)
        ]
        return str.join(valList)
