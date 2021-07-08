import enum

@enum.unique
class TemperatureOption(enum.Enum):
    DASH = "---"
    NO_HEAT = "No Heat"
    EXTRA_LOW = "Extra Low"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    
    def stringify(self, **kwargs):
        return self.value
