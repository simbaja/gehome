import enum

@enum.unique
class LaundrySubCycle(enum.Enum):
    DASH = "---"
    FILL = "Fill"
    SOAK = "Soak"
    WASH = "Wash"
    RINSE = "Rinse"
    SPIN = "Spin"
    DRAIN = "Drain"
    EXTRA_SPIN = "Extra Spin"
    EXTRA_RINSE = "Extra Rinse"
    TUMBLE = "Tumble"
    LOAD_SIZE_DETECTION = "Load Size Detection"
    DRYING = "Drying"
    MIST_STEAM = "Mist Steam"
    COOL_DOWN = "Cool Down"
    EXTENDED_TUMBLE = "Extended Tumble"
    DAMP = "Damp"
    AIR_FLUFF = "Air Fluff"
    
    def stringify(self, **kwargs):
        return self.name.replace("STATUS_","").replace("_"," ").title()
