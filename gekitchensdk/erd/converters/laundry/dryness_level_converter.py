import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdDrynessLevel, ErdDrynessNewLevel, DrynessLevel, DRYNESS_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class DrynessLevelConverter(ErdReadOnlyConverter[DrynessLevel]):
    def erd_decode(self, value: str) -> DrynessLevel:
        try:
            om = ErdDrynessLevel(erd_decode_int(value))
            return DRYNESS_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return ErdDrynessLevel.NA
