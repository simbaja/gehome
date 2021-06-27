import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdTankStatus, TankStatus, TANK_STATUS_MAP

_LOGGER = logging.getLogger(__name__)

class TankStatusConverter(ErdReadOnlyConverter[TankStatus]):
    def erd_decode(self, value: str) -> TankStatus:
        try:
            om = ErdTankStatus(erd_decode_int(value))
            return TANK_STATUS_MAP[om].value
        except (KeyError, ValueError):
            return ErdTankStatus.EMPTY
