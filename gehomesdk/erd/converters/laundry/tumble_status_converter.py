import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdTumbleStatus

_LOGGER = logging.getLogger(__name__)

class TumbleStatusConverter(ErdReadOnlyConverter[ErdTumbleStatus]):
    def erd_decode(self, value: str) -> ErdTumbleStatus:
        try:
            return ErdTumbleStatus(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdTumbleStatus.NOT_AVAILABLE
