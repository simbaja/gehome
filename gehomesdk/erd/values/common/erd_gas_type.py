import enum

@enum.unique
class ErdGasType(enum.Enum):
    """The type of gas connected to an appliance."""
    UNKNOWN = 0
    NATURAL_GAS = 1
    LIQUID_PROPANE = 2
