import enum
from typing import NamedTuple, Optional

@enum.unique
class ErdSmartDispenseSubstanceType(enum.Enum):
    DETERGENT = 0
    SOFTENER = 1

@enum.unique
class ErdSmartDispenseFlowBucket(enum.Enum):
    FLOW_RATE_BUCKET_ONE = 0
    FLOW_RATE_BUCKET_TWO = 1
    FLOW_RATE_BUCKET_THREE = 2
    FLOW_RATE_BUCKET_FOUR = 3
    FLOW_RATE_BUCKET_FIVE = 4
    FLOW_RATE_BUCKET_SIX = 5

@enum.unique
class ErdSmartDispenseDosageType(enum.Enum):
    OFF = 0
    LESS = 1
    MORE = 2
    AUTO = 3
    LESS_MINUS = 4
    REGULAR = 5
    MORE_PLUS = 6
    
class ErdSmartDispenseAdjustabilityOption (NamedTuple):
    substance: ErdSmartDispenseSubstanceType = ErdSmartDispenseSubstanceType.DETERGENT
    bucket: ErdSmartDispenseFlowBucket = ErdSmartDispenseFlowBucket.FLOW_RATE_BUCKET_ONE
    dosage: ErdSmartDispenseDosageType = ErdSmartDispenseDosageType.OFF
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"SmartDispenseAdjustabilityOption: Substance:{self.substance}, Bucket:{self.bucket}, Dosag:{self.dosage}"
