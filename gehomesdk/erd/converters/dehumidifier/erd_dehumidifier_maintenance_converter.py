import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.dehumidifier import ErdDehumidifierMaintenance

_LOGGER = logging.getLogger(__name__)

class ErdDehumidifierMaintenanceConverter(ErdReadOnlyConverter[ErdDehumidifierMaintenance]):
    def erd_decode(self, value: str) -> ErdDehumidifierMaintenance:
        if not value:
            return ErdDehumidifierMaintenance()
        
        try:
            #convert to int
            i = erd_decode_int(value)

            return ErdDehumidifierMaintenance(
                empty_bucket = bool((i & 0x01)),
                clean_filter = bool((i & 0x02 ) >> 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct maintenance tasks, using default.")
            return ErdDehumidifierMaintenance(raw_value=value)
