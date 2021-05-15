import enum

@enum.unique
class SoilLevel(enum.Enum):
    DASH = "---"
    EXTRA_LIGHT = "Extra Light"
    LIGHT = "Light"
    NORMAL = "Normal"
    HEAVY = "Heavy"
    EXTRA_HEAVY = "Extra Heavy"
    
    def stringify(self, **kwargs):
        return self.name.replace("STATUS_","").replace("_"," ").title()
