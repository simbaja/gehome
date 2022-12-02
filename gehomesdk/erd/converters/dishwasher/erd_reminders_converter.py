import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.dishwasher import ErdReminders

_LOGGER = logging.getLogger(__name__)

class ErdRemindersSettingConverter(ErdReadOnlyConverter[ErdReminders]):
    def erd_decode(self, value: str) -> ErdReminders:
        if not value:
            return ErdReminders()
        
        try:
            #convert to int
            i = erd_decode_int(value)

            return ErdReminders(
                clean_filter = bool((i & 0x01)),
                add_rinse_aid = bool((i & 0x02 ) >> 1),
                sanitized = bool((i & 0x04) >> 2),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct reminders, using default.")
            return ErdReminders(raw_value=value)
