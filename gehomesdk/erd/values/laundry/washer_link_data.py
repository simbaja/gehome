import enum
from typing import NamedTuple, Optional

@enum.unique
class BaseCycleType(enum.Enum):
    UNKNOWN = 0
    ATHLETIC_WEAR = 1
    BULKY = 2
    MIXED = 3
    COTTON = 4
    DELICATES = 5
    SPEED = 6
    TOWELS = 7
    SHEETS = 8
    COMFORTER = 9
    SANITIZE = 10
    JEANS = 11
    CASUAL_OR_PERM_PRESS = 12
    
    
class ErdWasherLinkData (NamedTuple):
    washer_cycle_count: int = 0
    water_extraction_level_index: int = 0
    washer_load_size_index: int = 0
    base_cycle_type: BaseCycleType = BaseCycleType.UNKNOWN
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"Washer Cycle Count:{self.washer_cylce_count}, Water Extraction Level Index:{self.water_extraction_level_index}, Washer Load Size Index:{self.washer_load_size_index}, Base Cycle Type:{self.base_cyle_type}"
