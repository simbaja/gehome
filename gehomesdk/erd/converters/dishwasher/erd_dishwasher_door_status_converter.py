import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.dishwasher import ErdDishwasherDoorStatus

_LOGGER = logging.getLogger(__name__)

class ErdDishwasherDoorStatusConverter(ErdReadOnlyConverter[ErdDishwasherDoorStatus]):
    def erd_decode(self, value: str) -> ErdDishwasherDoorStatus:
        """ Decodes the dishwasher door state """    
        try:  
            return ErdDishwasherDoorStatus(erd_decode_int(value))          
        except (ValueError, KeyError):
            return ErdDishwasherDoorStatus.NA
