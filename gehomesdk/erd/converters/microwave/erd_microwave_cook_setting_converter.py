import logging
from typing import List
from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values.microwave import ErdMicrowaveCookSetting

_LOGGER = logging.getLogger(__name__)

class ErdMicrowaveCookSettingConverter(ErdReadWriteConverter[ErdMicrowaveCookSetting]):
    def erd_decode(self, value: str) -> ErdMicrowaveCookSetting:
        if not value:
            return ErdMicrowaveCookSetting()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))
            
            return ErdMicrowaveCookSetting(
                target_power_level=int_values[0],
                cook_minutes=int_values[1],
                cook_seconds=int_values[2],
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct cook setting, using default.")
            return ErdMicrowaveCookSetting(raw_value=value)
    def erd_encode(self, value: ErdMicrowaveCookSetting) -> str:
        valList: List[str] = [
            erd_encode_int(value.target_power_level, 1),
            erd_encode_int(value.cook_minutes, 1),
            erd_encode_int(value.cook_seconds, 1)
        ]
        return str.join(valList)
