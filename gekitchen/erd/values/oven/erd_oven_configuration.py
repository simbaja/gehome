import enum

@enum.unique
class ErdOvenConfiguration(enum.Enum):
    """Representation of oven configurations."""
    HAS_KNOB = 1
    HAS_WARMING_DRAWER = 2
    HAS_LIGHT_BAR = 4
    HAS_LOWER_OVEN = 8
    HAS_LOWER_OVEN_KITCHEN_TIMER = 16
