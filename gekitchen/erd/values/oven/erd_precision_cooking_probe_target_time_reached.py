import enum

# This doesn't actually appear to be used anywhere in the app, so not
# sure which is Yes or No...
@enum.unique
class ErdPrecisionCookingProbeTargetTimeReached(enum.Enum):
    NA  = -1
    NO  = 0
    YES = 1
