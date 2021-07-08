import enum

@enum.unique
class WashTempLevel(enum.Enum):
    DASH = "---"
    TAP_COLD = "Tap Cold"
    COLD = "Cold"
    WARM = "Warm"
    HOT = "Hot"
    COOL = "Cool"
    COLORS = "Colors"
    EXTRA_HOT = "Extra Hot"
    
    def stringify(self, **kwargs):
        return self.value
