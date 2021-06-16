import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.advantium import ErdAdvantiumCookStatus
from gehomesdk.erd.values.advantium.advantium_enums import *

_LOGGER = logging.getLogger(__name__)

class ErdAdvantiumCookStatusConverter(ErdReadOnlyConverter[ErdAdvantiumCookStatus]):
    def erd_decode(self, value: str) -> ErdAdvantiumCookStatus:
        if not value:
            return ErdAdvantiumCookStatus()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))
            
            return ErdAdvantiumCookStatus(
                cook_action = CookAction(int_values[1]),
                cook_mode = CookMode(int_values[2]),
                termination_reason = TerminationReason(int_values[3]),
                preheat_status = PreheatStatus(int_values[4]),
                temperature = erd_decode_int(values[5] + values[6]),
                power_level = int_values[9],
                door_status = DoorStatus(int_values[11]),
                sensing_active = SensingActive(int_values[12]),
                cooling_fan_status = CoolingFanStatus(int_values[13]),
                oven_light_status = OvenLightStatus(int_values[14]),
                warm_status = WarmStatus(int_values[15]),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct cook status, using default.")
            return ErdAdvantiumCookStatus(raw_value=value)
