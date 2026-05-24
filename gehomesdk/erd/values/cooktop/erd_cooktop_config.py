import enum

# Note: From what I see through the code, the only check that is done
# is whether the config is non-zero.  We'll just coalesce all other
# values to present for now.
@enum.unique
class ErdCooktopConfig(enum.Enum):
    NONE = 0
    PRESENT = 1
    UNKNOWN = 255
