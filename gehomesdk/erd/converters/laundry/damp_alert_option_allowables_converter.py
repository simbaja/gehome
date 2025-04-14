import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdDampAlertOptionAllowables

_LOGGER = logging.getLogger(__name__)

class ErdDampAlertOptionAllowablesConverter(ErdReadOnlyConverter[ErdDampAlertOptionAllowables]):
    def erd_decode(self, value: str) -> ErdDampAlertOptionAllowables:
        if not value:
            return ErdDampAlertOptionAllowables()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdDampAlertOptionAllowables(
                damp_alert_disable_allowed = bool((i >> 8) & 1),
                damp_alert_enable_allowed = bool((i >> 9) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct damp alert option allowables, using default.")
            return ErdDampAlertOptionAllowables(raw_value=value)
