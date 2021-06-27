import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdTankSelected, TankSelected, TANK_SELECTED_MAP

_LOGGER = logging.getLogger(__name__)

class TankSelectedConverter(ErdReadOnlyConverter[TankSelected]):
    def erd_decode(self, value: str) -> TankSelected:
        try:
            om = ErdTankSelected(erd_decode_int(value))
            return TANK_SELECTED_MAP[om].value
        except (KeyError, ValueError):
            return ErdTankSelected.INVALID
