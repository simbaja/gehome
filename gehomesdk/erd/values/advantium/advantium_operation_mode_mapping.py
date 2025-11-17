from .advantium_enums import AdvantiumCookMode, AdvantiumWarmStatus
from .advantium_cook_setting import AdvantiumCookSetting
from .advantium_operation_mode import AdvantiumOperationMode

ADVANTIUM_OPERATION_MODE_COOK_SETTING_MAPPING = {
    AdvantiumOperationMode.OFF: AdvantiumCookSetting(AdvantiumCookMode.NO_MODE, None, None, None, None),
    AdvantiumOperationMode.CONVECTION_BAKE: AdvantiumCookSetting(AdvantiumCookMode.CONVECTION_BAKE, None, 350, 350, None, 900, True),
    AdvantiumOperationMode.BROIL: AdvantiumCookSetting(AdvantiumCookMode.BROIL, None, None, None, None),
    AdvantiumOperationMode.MICROWAVE_PL3: AdvantiumCookSetting(AdvantiumCookMode.MICROWAVE, None, None, None, 3, 60),
    AdvantiumOperationMode.MICROWAVE_PL5: AdvantiumCookSetting(AdvantiumCookMode.MICROWAVE, None, None, None, 5, 60),
    AdvantiumOperationMode.MICROWAVE_PL7: AdvantiumCookSetting(AdvantiumCookMode.MICROWAVE, None, None, None, 7, 60),
    AdvantiumOperationMode.MICROWAVE_PL10: AdvantiumCookSetting(AdvantiumCookMode.MICROWAVE, None, None, None, 10, 60),
    AdvantiumOperationMode.MICROWAVE_SENSOR: AdvantiumCookSetting(AdvantiumCookMode.MICROWAVE_SENSOR, None, None, None, None),
    AdvantiumOperationMode.WARM_CRISP_LOW: AdvantiumCookSetting(AdvantiumCookMode.WARM, AdvantiumWarmStatus.CRISP, 140, 155, None),
    AdvantiumOperationMode.WARM_CRISP_MED: AdvantiumCookSetting(AdvantiumCookMode.WARM, AdvantiumWarmStatus.CRISP, 165, 185, None),
    AdvantiumOperationMode.WARM_CRISP_HIGH: AdvantiumCookSetting(AdvantiumCookMode.WARM, AdvantiumWarmStatus.CRISP, 195, 225, None),
    AdvantiumOperationMode.WARM_MOIST_LOW: AdvantiumCookSetting(AdvantiumCookMode.WARM, AdvantiumWarmStatus.MOIST, 140, 155, None),
    AdvantiumOperationMode.WARM_MOIST_MED: AdvantiumCookSetting(AdvantiumCookMode.WARM, AdvantiumWarmStatus.MOIST, 165, 185, None),
    AdvantiumOperationMode.WARM_MOIST_HIGH: AdvantiumCookSetting(AdvantiumCookMode.WARM, AdvantiumWarmStatus.MOIST, 195, 225, None),    
    AdvantiumOperationMode.PROOF: AdvantiumCookSetting(AdvantiumCookMode.PROOF, None, None, None, None),
    AdvantiumOperationMode.TOAST: AdvantiumCookSetting(AdvantiumCookMode.TOAST, None, None, None, None),
    AdvantiumOperationMode.MICROWAVE_SLOW_COOK: AdvantiumCookSetting(AdvantiumCookMode.MICROWAVE_SLOW_COOK, None, None, None, None, 3600)
}
