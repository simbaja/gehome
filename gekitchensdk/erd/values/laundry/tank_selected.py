import enum

@enum.unique
class TankSelected(enum.Enum):
    DASH = "---"
    DETERGENT = "Detergent"
    SOFTENER = "Softener"
    BLEACH = "Bleach"
    OTHER = "Other"
