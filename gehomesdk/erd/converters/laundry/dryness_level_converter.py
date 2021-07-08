import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdDrynessLevel, ErdDrynessNewLevel, DrynessLevel, DRYNESS_LEVEL_MAP, DRYNESSNEW_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class DrynessLevelConverter(ErdReadOnlyConverter[DrynessLevel]):
    def erd_decode(self, value: str) -> DrynessLevel:
        try:
            om = ErdDrynessLevel(erd_decode_int(value))
            return DRYNESS_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return DrynessLevel.DASH

class DrynessNewLevelConverter(ErdReadOnlyConverter[DrynessLevel]):
    def erd_decode(self, value: str) -> DrynessLevel:
        try:
            om = ErdDrynessNewLevel(erd_decode_int(value))
            return DRYNESSNEW_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return DrynessLevel.DASH
