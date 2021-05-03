import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdLaundryOperatingMode, LaundryOperatingMode, LAUNDRY_OPERATING_MODE_MAP

_LOGGER = logging.getLogger(__name__)

class LaundryOperatingModeConverter(ErdReadOnlyConverter[LaundryOperatingMode]):
    def erd_decode(self, value: str) -> LaundryOperatingMode:
        """Decode the dishwasher operating state """
        try:
            om = ErdLaundryOperatingMode(erd_decode_int(value))
            _LOGGER.debug(f'raw operating mode value: {om}')
            return LAUNDRY_OPERATING_MODE_MAP[om].value
        except (KeyError, ValueError):
            return ErdLaundryOperatingMode.NA
