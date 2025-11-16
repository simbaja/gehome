import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdLaundryCycle

_LOGGER = logging.getLogger(__name__)

class ErdLaundryCycleConverter(ErdReadOnlyConverter[ErdLaundryCycle]):
    def erd_decode(self, value: str) -> ErdLaundryCycle:
        try:
            return ErdLaundryCycle(erd_decode_int(value))
        except (KeyError, ValueError):
            _LOGGER.info(f"Unknown laundry cycle found, value = {value}")
            return ErdLaundryCycle.NOT_DEFINED
