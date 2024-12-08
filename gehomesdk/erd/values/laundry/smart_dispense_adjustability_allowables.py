import enum
from typing import NamedTuple, Optional
    
class ErdSmartDispenseAdjustabilityAllowables (NamedTuple):
    detergent_bucket_one_allowed: bool = False
    detergent_bucket_two_allowed: bool = False
    detergent_bucket_three_allowed: bool = False
    detergent_bucket_four_allowed: bool = False
    softener_bucket_one_allowed: bool = False
    softener_bucket_two_allowed: bool = False
    softener_bucket_three_allowed: bool = False
    softener_bucket_four_allowed: bool = False
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"SmartDispenseAdjustabilityAllowables: Detergent1:{self.detergent_bucket_one}, Detergent2:{self.detergent_bucket_two}, Detergent3:{self.detergent_bucket_three}, Detergent4:{self.detergent_bucket_four}, Softener1:{self.softener_bucket_one_allowed}, Softener2:{self.softener_bucket_two_allowed}, Softener3:{self.softener_bucket_three_allowed}, Softener4:{self.softener_bucket_four_allowed}"
    
