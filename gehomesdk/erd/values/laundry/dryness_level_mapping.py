from .laundry_enums import ErdDrynessLevel, ErdDrynessNewLevel
from .dryness_level import DrynessLevel

DRYNESS_LEVEL_MAP = {
    ErdDrynessLevel.DAMP: DrynessLevel.DAMP,
    ErdDrynessLevel.LESS_DRY: DrynessLevel.LESS_DRY,
    ErdDrynessLevel.DRY_DRY: DrynessLevel.DRY,
    ErdDrynessLevel.MORE_DRY: DrynessLevel.MORE_DRY,
    ErdDrynessLevel.EXTRA_DRY: DrynessLevel.EXTRA_DRY,
    ErdDrynessLevel.INVALID: DrynessLevel.DASH
}

DRYNESSNEW_LEVEL_MAP = {
    ErdDrynessNewLevel.DAMP: DrynessLevel.DAMP,
    ErdDrynessNewLevel.LESS_DRY: DrynessLevel.LESS_DRY,
    ErdDrynessNewLevel.DRY_DRY: DrynessLevel.DRY,
    ErdDrynessNewLevel.MORE_DRY: DrynessLevel.MORE_DRY,
    ErdDrynessNewLevel.EXTRA_DRY: DrynessLevel.EXTRA_DRY,
    ErdDrynessNewLevel.INVALID: DrynessLevel.DASH
}
