import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdDryerDrynessOptionAllowables

_LOGGER = logging.getLogger(__name__)

class ErdDryerDrynessOptionAllowablesConverter(ErdReadOnlyConverter[ErdDryerDrynessOptionAllowables]):
    def erd_decode(self, value: str) -> ErdDryerDrynessOptionAllowables:
        if not value:
            return ErdDryerDrynessOptionAllowables()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdDryerDrynessOptionAllowables(
                dryness_option_disabled_allowed = bool((i >> 8) & 1),
                dryness_option_damp_allowed = bool((i >> 9) & 1),
                dryness_option_lessdry_allowed = bool((i >> 10) & 1),
                dryness_option_dry_allowed = bool((i >> 11) & 1),
                dryness_option_moredry_allowed = bool((i >> 12) & 1),
                dryness_option_extradry_allowed = bool((i >> 13) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct dryer dryness option allowables, using default.")
            return ErdDryerDrynessOptionAllowables(raw_value=value)
