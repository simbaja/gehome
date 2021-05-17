import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdTankStatus, TankStatus, TANK_STATUS_MAP

_LOGGER = logging.getLogger(__name__)

class TankStatusConverter(ErdReadOnlyConverter[TankStatus]):
    def erd_decode(self, value: str) -> TankStatus:
        try:
            om = ErdTankStatus(erd_decode_int(value))
            return TANK_STATUS_MAP[om].value
        except (KeyError, ValueError):
            return ErdTankStatus.NA
