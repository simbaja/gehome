import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdTankSelected, TankSelected, TANK_SELECTED_MAP

_LOGGER = logging.getLogger(__name__)

class TankSelectedConverter(ErdReadOnlyConverter[TankSelected]):
    def erd_decode(self, value: str) -> TankSelected:
        try:
            om = ErdTankSelected(erd_decode_int(value))
            return TANK_SELECTED_MAP[om].value
        except (KeyError, ValueError):
            return ErdTankSelected.NA
