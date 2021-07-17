from gehomesdk.erd.values.advantium.advantium_enums import CookMode
from .advantium_cook_setting import AdvantiumCookSetting
from .advantium_operation_mode import AdvantiumOperationMode

ADVANTIUM_OPERATION_MODE_COOK_SETTING_MAPPING = {
    AdvantiumOperationMode.OFF: AdvantiumCookSetting(CookMode.NO_MODE, None, None, None, None),
    AdvantiumOperationMode.CONVECTION_BAKE: AdvantiumCookSetting(CookMode.CONVECTION_BAKE, None, 350, 350, None, 900, True),
    AdvantiumOperationMode.BROIL: AdvantiumCookSetting(CookMode.BROIL, None, None, None, None),
    AdvantiumOperationMode.MICROWAVE_PL3: AdvantiumCookSetting(CookMode.MICROWAVE, None, None, None, 3, 60),
    AdvantiumOperationMode.MICROWAVE_PL5: AdvantiumCookSetting(CookMode.MICROWAVE, None, None, None, 5, 60),
    AdvantiumOperationMode.MICROWAVE_PL7: AdvantiumCookSetting(CookMode.MICROWAVE, None, None, None, 7, 60),
    AdvantiumOperationMode.MICROWAVE_PL10: AdvantiumCookSetting(CookMode.MICROWAVE, None, None, None, 10, 60),
    AdvantiumOperationMode.MICROWAVE_SENSOR: AdvantiumCookSetting(CookMode.MICROWAVE_SENSOR, None, None, None, None),
    AdvantiumOperationMode.WARM_CRISP_LOW: AdvantiumCookSetting(CookMode.WARM, None, 140, 155, None),
    AdvantiumOperationMode.WARM_CRISP_MED: AdvantiumCookSetting(CookMode.WARM, None, 165, 185, None),
    AdvantiumOperationMode.WARM_CRISP_HIGH: AdvantiumCookSetting(CookMode.WARM, None, 195, 225, None),
    AdvantiumOperationMode.WARM_MOIST_LOW: AdvantiumCookSetting(CookMode.WARM, None, 140, 155, None),
    AdvantiumOperationMode.WARM_MOIST_MED: AdvantiumCookSetting(CookMode.WARM, None, 165, 185, None),
    AdvantiumOperationMode.WARM_MOIST_HIGH: AdvantiumCookSetting(CookMode.WARM, None, 195, 225, None),
    AdvantiumOperationMode.PROOF: AdvantiumCookSetting(CookMode.PROOF, None, None, None, None),
    AdvantiumOperationMode.TOAST: AdvantiumCookSetting(CookMode.TOAST, None, None, None, None),
    AdvantiumOperationMode.MICROWAVE_SLOW_COOK: AdvantiumCookSetting(CookMode.MICROWAVE_SLOW_COOK, None, None, None, None, 3600)
}
