import enum

@enum.unique
class DrynessLevel(enum.Enum):
    DASH = "---"
    DAMP = "Damp"
    LESS_DRY = "Less Dry"
    DRY = "Dry"
    MORE_DRY = "More Dry"
    EXTRA_DRY = "Extra Dry"
    
    def stringify(self, **kwargs):
        return self.value
