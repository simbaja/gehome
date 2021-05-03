import enum

@enum.unique
class ErdDrynessNewLevel(enum.Enum):
    DAMP = 1
    LESS_DRY = 2
    DRY_DRY = 3
    MORE_DRY = 4
    EXTRA_DRY = 5
    INVALID = 0
