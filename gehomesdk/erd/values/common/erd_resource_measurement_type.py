import enum

@enum.unique
class ErdResourceMeasurementType(enum.Enum):
    """Whether an appliance's reported resource usage is estimated or directly measured."""
    ESTIMATED = 0
    MEASURED = 1
