from .erd_drynessnew_level import ErdDrynessNewLevel
from .drynessnew_level import DrynessNewLevel

DRYNESSNEW_LEVEL_MAP = {
    ErdDrynessNewLevel.DAMP: DrynessNewLevel.DAMP,
    ErdDrynessNewLevel.LESS_DRY: DrynessNewLevel.LESS_DRY,
    ErdDrynessNewLevel.DRY_DRY: DrynessNewLevel.DRY,
    ErdDrynessNewLevel.MORE_DRY: DrynessNewLevel.MORE_DRY,
    ErdDrynessNewLevel.EXTRA_DRY: DrynessNewLevel.EXTRA_DRY,
    ErdDrynessNewLevel.INVALID: DrynessNewLevel.DASH
}
