import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdDrynessLevel, ErdDrynessNewLevel, DrynessLevel, DRYNESS_LEVEL_MAP, DRYNESSNEW_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class DrynessLevelConverter(ErdReadOnlyConverter[DrynessLevel]):
    def erd_decode(self, value: str) -> DrynessLevel:
        try:
            om = ErdDrynessLevel(erd_decode_int(value))
            return DRYNESS_LEVEL_MAP[om]
        except (KeyError, ValueError):
            return DrynessLevel.DASH

class DrynessNewLevelConverter(ErdReadOnlyConverter[DrynessLevel]):
    def erd_decode(self, value: str) -> DrynessLevel:
        try:
            om = ErdDrynessNewLevel(erd_decode_int(value))
            return DRYNESSNEW_LEVEL_MAP[om]
        except (KeyError, ValueError):
            return DrynessLevel.DASH
