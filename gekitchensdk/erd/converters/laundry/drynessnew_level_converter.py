import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdDrynessNewLevel, DrynessNewLevel, DRYNESSNEW_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class DrynessNewLevelConverter(ErdReadOnlyConverter[DrynessNewLevel]):
    def erd_decode(self, value: str) -> DrynessNewLevel:
        try:
            om = ErdDrynessNewLevel(erd_decode_int(value))
            return DRYNESSNEW_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return ErdDrynessNewLevel.NA
