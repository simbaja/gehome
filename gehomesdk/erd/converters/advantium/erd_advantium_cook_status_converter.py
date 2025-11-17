import logging

from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.advantium import ErdAdvantiumCookStatus
from ...values.advantium.advantium_enums import *

_LOGGER = logging.getLogger(__name__)

class ErdAdvantiumCookStatusConverter(ErdReadOnlyConverter[ErdAdvantiumCookStatus]):
    def erd_decode(self, value: str) -> ErdAdvantiumCookStatus:
        if not value:
            return ErdAdvantiumCookStatus()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))

            cook_status = ErdAdvantiumCookStatus(
                cook_action = AdvantiumCookAction(int_values[1]),
                cook_mode = AdvantiumCookMode(int_values[2]),
                termination_reason = AdvantiumTerminationReason(int_values[3]),
                preheat_status = AdvantiumPreheatStatus(int_values[4]),
                temperature = erd_decode_int(values[5] + values[6]),
                power_level = int_values[9],
                door_status = AdvantiumDoorStatus(int_values[11]),
                sensing_active = AdvantiumSensingActive(int_values[12]),
                cooling_fan_status = AdvantiumCoolingFanStatus(int_values[13]),
                oven_light_status = AdvantiumOvenLightStatus(int_values[14]),
                warm_status = AdvantiumWarmStatus(int_values[15]),
                raw_value=value
            )
            _LOGGER.debug("Cook Status for value %s is: %s", value, cook_status)
            return cook_status
        except Exception as ex: 
            _LOGGER.exception("Could not construct cook status (value: %s), using default.")
            return ErdAdvantiumCookStatus(raw_value=value)
