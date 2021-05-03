import enum

@enum.unique
class RinseOption(enum.Enum):
    INVALID = "---"
    NORMAL = "Normal"
    EXTRA = "Extra"
    MAX = "Max"
    HEAVY = "Heavy"
    EXTRA_HEAVY = "Extra Heavy"
    
    def stringify(self, **kwargs):
        return self.name.replace("STATUS_","").replace("_"," ").title()
