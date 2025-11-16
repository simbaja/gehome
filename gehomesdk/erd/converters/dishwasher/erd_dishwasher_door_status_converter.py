import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.dishwasher import ErdDishwasherDoorStatus

_LOGGER = logging.getLogger(__name__)

class ErdDishwasherDoorStatusConverter(ErdReadOnlyConverter[ErdDishwasherDoorStatus]):
    def erd_decode(self, value: str) -> ErdDishwasherDoorStatus:
        """ Decodes the dishwasher door state """    
        try:  
            return ErdDishwasherDoorStatus(erd_decode_int(value))          
        except (ValueError, KeyError):
            return ErdDishwasherDoorStatus.NA
