import enum

@enum.unique
class SpinTimeLevel(enum.Enum):
    DASH = "---"
    NO_SPIN = "No Spin"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    EXTRA_HIGH = "Extra High"
    
    def stringify(self, **kwargs):
        return self.name.replace("STATUS_","").replace("_"," ").title()
