import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdLaundryDoorLockStatus, LaundryDoorLockStatus, LAUNDRY_DOOR_LOCK_STATUS_MAP

_LOGGER = logging.getLogger(__name__)

class LaundryDoorLockStatusConverter(ErdReadOnlyConverter[LaundryDoorLockStatus]):
    def erd_decode(self, value: str) -> LaundryDoorLockStatus:
        """Decode the dishwasher operating state """
        try:
            om = ErdLaundryDoorLockStatus(erd_decode_int(value))
            ###_LOGGER.debug(f'raw operating mode value: {om}')
            return LAUNDRY_DOOR_LOCK_STATUS_MAP[om].value
        except (KeyError, ValueError):
            return ErdLaundryDoorLockStatus.NA
