import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdTankSelected

_LOGGER = logging.getLogger(__name__)

class TankSelectedConverter(ErdReadOnlyConverter[ErdTankSelected]):
    def erd_decode(self, value: str) -> ErdTankSelected:
        try:
            return ErdTankSelected(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdTankSelected.INVALID
