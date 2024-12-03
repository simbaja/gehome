import enum

@enum.unique
class SpinSpeedOption(enum.Enum):
    DASH = "---"
    NO_SPIN = "No Spin"
    FIVEHUNDRED = "500"
    EIGHTHUNDRED = "800"
    ELEVENHUNDRED = "1100"
    FOURTEENHUNDRED = "1400"
    
    def stringify(self, **kwargs):
        return self.value
