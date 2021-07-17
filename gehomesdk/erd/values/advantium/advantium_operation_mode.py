import enum
from enum import auto
from typing import Optional

@enum.unique
class AdvantiumOperationMode(enum.Enum):
    OFF = "---"
    CONVECTION_BAKE = "Convection Bake"
    BROIL = "Broil"
    MICROWAVE_PL3 = "Microwave PL3"
    MICROWAVE_PL5 = "Microwave PL5"
    MICROWAVE_PL7 = "Microwave PL7"
    MICROWAVE_PL10 = "Microwave PL10"
    MICROWAVE_SENSOR = "Microwave Sensor"
    WARM_CRISP_LOW = "Warm [Crisp/Low]"
    WARM_CRISP_MED = "Warm [Crisp/Medium]"
    WARM_CRISP_HIGH = "Warm [Crisp/High]"
    WARM_MOIST_LOW = "Warm [Moist/Low]"
    WARM_MOIST_MED = "Warm [Moist/Medium]"
    WARM_MOIST_HIGH = "Warm [Moist/High]"
    PROOF = "Proof"
    TOAST = "Toast"
    MICROWAVE_SLOW_COOK = "Microwave Slow Cook"

    def stringify(self, **kwargs):
        return self.value
