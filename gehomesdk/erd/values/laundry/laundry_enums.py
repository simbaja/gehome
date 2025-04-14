import enum
from typing import NamedTuple, Optional

@enum.unique
class ErdDrynessLevel(enum.Enum):
    DAMP = 0
    LESS_DRY = 1
    DRY_DRY = 2
    MORE_DRY = 3
    EXTRA_DRY = 4
    INVALID = 5

@enum.unique
class ErdDrynessNewLevel(enum.Enum):
    DAMP = 1
    LESS_DRY = 2
    DRY_DRY = 3
    MORE_DRY = 4
    EXTRA_DRY = 5
    INVALID = 0

@enum.unique
class ErdLaundryCycle(enum.Enum):
    NOT_DEFINED = 0
    BASKET_CLEAN = 1
    DRAIN_AND_SPIN = 2
    QUICK_RINSE = 3
    BULKY_ITEMS = 4
    SANITIZE = 5
    TOWELS_OR_SHEETS = 6
    WASHER_STEAM_REFRESH = 7
    NORMAL_OR_MIXED_LOAD = 8
    WHITES = 9
    DARK_COLORS = 10
    JEANS = 11
    HAND_WASH = 12
    DELICATES = 13
    SPEED_WASH = 14
    HEAVY_DUTY = 15
    ALLERGEN = 16
    POWER_CLEAN = 17
    RINSE_AND_SPIN = 18
    SINGLE_ITEM_WASH = 19
    COLORS = 20
    COLD_WASH = 21
    WATER_STATION = 22
    TUB_CLEAN = 23
    CASUALS_WITH_STEAM = 24
    STAIN_WASH_WITH_STEAM = 25
    DEEP_CLEAN = 26
    BULKY_BEDDING = 27
    NORMAL = 28
    QUICK_WASH = 29
    SANITIZE_WITH_OXI = 30
    SELF_CLEAN = 31
    TOWELS = 32
    SOAK = 33
    WOOL = 34
    ULTRA_FRESH_VENT = 35
    SANITIZE_PLUS_ALLERGEN = 36
    SPIN_ONLY = 37
    EVERYDAY = 38
    SOFT_TOYS = 39
    SNEAKERS = 40
    SYNTHETICS = 41
    SILK = 42
    DENIM = 43
    DRUM_CLEAN = 44
    SHEETS = 45
    QUICK_15 = 46
    QUICK_30 = 47
    EASY_IRON = 48
    SPORTS = 49
    ECO_40_TO_60 = 50
    TWENTY_C = 51
    WARM_WASH = 52
    HOT_WASH = 53
    SWIM_WEAR = 54
    ECO = 55
    EXPRESS = 56
    MIX = 57
    QUICK_CYCLE = 58
    DUVET = 59
    COTTONS = 128
    EASY_CARE = 129
    ACTIVE_WEAR = 130
    TIMED_DRY = 131
    DEWRINKLE = 132
    AIR_FLUFF = 133
    STEAM_REFRESH2 = 134
    STEAM_DEWRINKLE = 135
    SPEED_DRY = 136
    MIXED = 137
    QUICK_DRY = 138
    CASUALS = 139
    WARM_UP = 140
    ENERGY_SAVER = 141
    ANTIBACTERIAL = 142
    RACK_DRY = 143
    BABY_CARE = 144
    AUTO_DRY = 145
    AUTO_EXTRA_DRY = 146
    PERM_PRESS = 147
    WASHER_LINK = 148
    AUTO_DAMP_DRY = 149
    SMART_VENT = 150
    PRE_IRON = 151
    HYGIENE = 152
    COOL_AIR = 153
    OUTDOOR = 154
    ULTRA_DELICATE = 155
    SCENT = 156
    SANITIZE_STEAM = 157
    DURABLE = 158
    SHOES = 159
    SHIRTS = 160
    REFRESH = 161
    FRESHEN = 162
    ECO_COOL = 163
    RINSE_AND_DRY = 164
    LEATHER = 165
    OUTERWEAR = 166
    MIXED_REFRESH = 167
    SHIRTS_REFRESH = 168
    DELICATE_REFRESH = 169
    SANITISE_REFRESH = 170
    LIGHT = 171
    HEAVY = 172
    WOOL_OR_KNIT = 173
    RAIN_OR_SNOW = 174
    KIDS_ITEM = 175
    SUITS_OR_COATS = 176
    PANTS_CREASE = 177
    STEAM_NORMAL = 178
    STEAM_WHITES = 179
    STEAM_TOWELS = 180
    STEAM_SANITIZE = 181
    DOWN = 182
    NIGHT_DRY = 183
    QUIET = 184
    RESET = 255

    def stringify(self, **kwargs):
        if self == ErdLaundryCycle.NOT_DEFINED:
            return "---"
        return self.name.replace("_"," ").replace("2", "").title()      

@enum.unique
class ErdLaundryDoorStatus(enum.Enum):
    OPEN = 0
    CLOSED = 1
    UNKNOWN = 255

    def stringify(self, **kwargs):
        return self.name.title()      

    def boolify(self) -> Optional[bool]:
        return self == ErdLaundryDoorStatus.OPEN

@enum.unique
class ErdLaundrySubCycle(enum.Enum):
    CYCLE_NONE = 0
    FILL = 1
    SOAK = 2
    WASH = 3
    RINSE = 4
    SPIN = 5
    DRAIN = 6
    EXTRA_SPIN = 7
    EXTRA_RINSE = 8
    TUMBLE = 9
    LOAD_SIZE_DETECTION = 10
    DRYING = 128
    MIST_STEAM = 129
    COOL_DOWN = 130
    EXTENDED_TUMBLE = 131
    DAMP = 132
    AIR_FLUFF = 133

    def stringify(self, **kwargs):
        if self == ErdLaundrySubCycle.CYCLE_NONE:
            return "---"
        return self.name.replace("_"," ").title()    

@enum.unique
class ErdMachineState(enum.Enum):
    IDLE = 0
    STANDBY = 1
    RUN = 2
    PAUSE = 3
    END_OF_CYCLE = 4
    DSM_DELAY_RUN = 5
    DELAY_RUN = 6
    DELAY_PAUSE = 7
    DRAIN_TIMEOUT = 8
    COMMISSIONING = 9
    BULK_FLUSH = 10
    CLEAN_SPEAK = 128

@enum.unique
class ErdRinseOption(enum.Enum):
    INVALID = 0
    NORMAL = 1
    EXTRA = 2
    MAX = 3
    HEAVY = 4
    EXTRA_HEAVY = 5

    def stringify(self, **kwargs):
        if self == ErdRinseOption.INVALID:
            return "---"
        return self.name.replace("_"," ").title()        

class ErdSheetUsageConfiguration (NamedTuple):
    extra_large_load_size: int = 0
    large_load_size: int = 0
    medium_load_size: int = 0
    small_load_size: int = 0
    timed_dryer_sheets_load_size: int = 0
    raw_value: Optional[str] = None

    def stringify(self, **kwargs):
        return f"S:{self.small_load_size}, M:{self.medium_load_size}, L:{self.large_load_size}, XL:{self.extra_large_load_size}, Timed:{self.timed_dryer_sheets_load_size}"

class ErdSmartDispense (NamedTuple):
    loads_left: int = 0
    signal: int = 0
    raw_value: Optional[str] = None

@enum.unique
class ErdSmartDispenseTankStatus(enum.Enum):
    FULL = 2
    LOW = 1
    UNKNOWN = 0

    def stringify(self, **kwargs):
        if self == ErdSmartDispenseTankStatus.UNKNOWN:
            return "N/A"
        return self.name.replace("_", " ").title()

@enum.unique
class ErdSoilLevel(enum.Enum):
    EXTRA_LIGHT = 0
    LIGHT = 1
    NORMAL = 2
    HEAVY = 3
    EXTRA_HEAVY = 4
    INVALID = 5

    def stringify(self, **kwargs):
        if self == ErdSoilLevel.INVALID:
            return "---"
        return self.name.replace("_"," ").title()      

@enum.unique
class ErdSpinTimeLevel(enum.Enum):
    NO_SPIN = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    EXTRA_HIGH = 4
    DISABLE = 5

    def stringify(self, **kwargs):
        if self == ErdSpinTimeLevel.DISABLE:
            return "---"        
        return self.name.replace("_"," ").title()        

@enum.unique
class ErdTankSelected(enum.Enum):
    DETERGENT = 0
    SOFTENER = 1
    BLEACH = 2
    OTHER = 3
    INVALID = 4

    def stringify(self, **kwargs):
        if self == ErdTankSelected.INVALID:
            return "---"           
        return self.name.title()        

@enum.unique
class ErdTankStatus(enum.Enum):
    FULL = 100
    PERCENT_75 = 75
    PERCENT_50 = 50
    PERCENT_25 = 25
    EMPTY = 0

@enum.unique
class ErdTemperatureOption(enum.Enum):
    NO_HEAT = 0
    EXTRA_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    INVALID = 5

@enum.unique
class ErdTemperatureNewOption(enum.Enum):
    INVALID = 0
    NO_HEAT = 1
    EXTRA_LOW = 2
    LOW = 3
    MEDIUM = 4
    HIGH = 5

@enum.unique
class ErdTumbleStatus(enum.Enum):
    NOT_AVAILABLE = 255
    ENABLE = 1
    DISABLE = 0

    def stringify(self, **kwargs):
        if self == ErdTumbleStatus.NOT_AVAILABLE:
            return "N/A"
        return self.name.replace("_"," ").title()         

    def boolify(self) -> Optional[bool]:
        return self == ErdTumbleStatus.ENABLE

@enum.unique
class ErdWashTempLevel(enum.Enum):
    TAP_COLD_1 = 0
    COLD_1 = 1
    WARM_1 = 2
    HOT_1 = 3
    EXTRAHOT_1 = 4
    INVALID = 6
    TAP_COLD_2 = 16
    COLD_2 = 17
    COOL_2 = 18
    COLORS_2 = 19
    WARM_2 = 20
    HOT_2 = 21
    EXTRA_HOT_2 = 22

@enum.unique
class ErdWashStainRemovalGuideOption(enum.Enum):
    OFF = 0
    PROTEIN_BASED = 1
    TANNIN_BASED = 2
    SOIL_BASED = 3
    ACID_BASED = 4
    BEVERAGE = 5
    OIL_BASED = 6
    
@enum.unique
class ErdDownloadedCycleRequest(enum.Enum):
    NOT_DEFINED = 0
    BASKET_CLEAN = 1
    DRAIN_AND_SPIN = 2
    QUICK_RINSE = 3
    BULKY_ITEMS = 4
    SANITIZE = 5
    TOWELS_OR_SHEETS = 6
    WASHER_STEAM_REFRESH = 7
    NORMAL_OR_MIXED_LOAD = 8
    WHITES = 9
    DARK_COLORS = 10
    JEANS = 11
    HAND_WASH = 12
    DELICATES = 13
    SPEED_WASH = 14
    HEAVY_DUTY = 15
    ALLERGEN = 16
    POWER_CLEAN = 17
    RINSE_AND_SPIN = 18
    SINGLE_ITEM_WASH = 19
    COLORS = 20
    COLD_WASH = 21
    WATER_STATION = 22
    TUB_CLEAN = 23
    CASUALS_WITH_STEAM = 24
    STAIN_WASH_WITH_STEAM = 25
    DEEP_CLEAN = 26
    BULKY_BEDDING = 27
    NORMAL = 28
    QUICK_WASH = 29
    SANITIZE_WITH_OXI = 30
    SELF_CLEAN = 31
    TOWELS = 32
    SOAK = 33
    WOOL = 34
    ULTRA_FRESH_VENT = 35
    SANITIZE_PLUS_ALLERGEN = 36
    SPIN_ONLY = 37
    EVERYDAY = 38
    SOFT_TOYS = 39
    SNEAKERS = 40
    SYNTHETICS = 41
    SILK = 42
    DENIM = 43
    DRUM_CLEAN = 44
    SHEETS = 45
    QUICK_15 = 46
    QUICK_30 = 47
    EASY_IRON = 48
    SPORTS = 49
    ECO_40_TO_60 = 50
    TWENTY_C = 51
    WARM_WASH = 52
    HOT_WASH = 53
    SWIM_WEAR = 54
    ECO = 55
    EXPRESS = 56
    MIX = 57
    QUICK_CYCLE = 58
    DUVET = 59
    COTTONS = 128
    EASY_CARE = 129
    ACTIVE_WEAR = 130
    TIMED_DRY = 131
    DEWRINKLE = 132
    QUICK_OR_AIRFLUFF = 133
    STEAM_REFRESH = 134
    STEAM_DEWRINKLE = 135
    SPEED_DRY = 136
    MIXED = 137
    QUICK_DRY = 138
    CASUALS = 139
    WARM_UP = 140
    ENERGY_SAVER = 141
    ANTIBACTERIAL = 142
    RACK_DRY = 143
    BABY_CARE = 144
    AUTO_DRY = 145
    AUTO_EXTRA_DRY = 146
    PERM_PRESS = 147
    WASHER_LINK = 148
    AUTO_DAMP_DRY = 149
    SMART_VENT = 150
    PRE_IRON = 151
    HYGIENE = 152
    COOL_AIR = 153
    OUTDOOR = 154
    ULTRA_DELICATE = 155
    SCENT = 156
    SANITIZE_STEAM = 157
    DURABLE = 158
    SHOES = 159
    SHIRTS = 160
    REFRESH = 161
    FRESHEN = 162
    ECO_COOL = 163
    RINSE_AND_DRY = 164
    LEATHER = 165
    OUTERWEAR = 166
    MIXED_REFRESH = 167
    SHIRTS_REFRESH = 168
    DELICATE_REFRESH = 169
    SANITISE_REFRESH = 170
    LIGHT = 171
    HEAVY = 172
    WOOL_OR_KNIT = 173
    RAIN_OR_SNOW = 174
    KIDS_ITEM = 175
    SUITS_OR_COATS = 176
    PANTS_CREASE = 177
    STEAM_NORMAL = 178
    STEAM_WHITES = 179
    STEAM_TOWELS = 180
    STEAM_SANITIZE = 181
    DOWN = 182
    NIGHT_DRY = 183
    QUIET = 184
    RESET = 255

@enum.unique
class ErdRemoteStartExtendedTumble(enum.Enum):
    START_EXTENDED_TUMBLE = 0
    REQUEST_PROCESSED = 255

@enum.unique
class ErdDryerExtendedTumbleOptionRequest(enum.Enum):
    DISABLED = 0
    ENABLED = 1
    REQUEST_PROCESSED = 255
