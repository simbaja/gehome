import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdDryerExtendedTumbleOptionAllowables

_LOGGER = logging.getLogger(__name__)

class ErdDryerExtendedTumbleOptionAllowablesConverter(ErdReadOnlyConverter[ErdDryerExtendedTumbleOptionAllowables]):
    def erd_decode(self, value: str) -> ErdDryerExtendedTumbleOptionAllowables:
        if not value:
            return ErdDryerExtendedTumbleOptionAllowables()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdDryerExtendedTumbleOptionAllowables(
                dryer_extended_tumble_disable_allowed = bool((i >> 8) & 1),
                dryer_extended_tumble_enable_allowed = bool((i >> 9) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct dryer extended tumble option allowables, using default.")
            return ErdDryerExtendedTumbleOptionAllowables(raw_value=value)
