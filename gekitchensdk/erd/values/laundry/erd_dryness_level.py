import enum

@enum.unique
class ErdDrynessLevel(enum.Enum):
    DAMP = 0
    LESS_DRY = 1
    DRY_DRY = 2
    MORE_DRY = 3
    EXTRA_DRY = 4
    INVALID = 5

@enum.unique
class ErdDrynessNewLevel(enum.Enum):
    DAMP = 1
    LESS_DRY = 2
    DRY_DRY = 3
    MORE_DRY = 4
    EXTRA_DRY = 5
    INVALID = 0
