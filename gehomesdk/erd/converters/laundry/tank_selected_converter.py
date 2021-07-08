import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdTankSelected

_LOGGER = logging.getLogger(__name__)

class TankSelectedConverter(ErdReadOnlyConverter[ErdTankSelected]):
    def erd_decode(self, value: str) -> ErdTankSelected:
        try:
            return ErdTankSelected(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdTankSelected.INVALID
