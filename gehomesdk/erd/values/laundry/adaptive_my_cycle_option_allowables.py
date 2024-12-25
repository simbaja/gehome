from typing import NamedTuple, Optional
    
class ErdAdaptiveMyCycleOptionAllowables (NamedTuple):
    adaptive_disable_allowed: bool = False
    adaptive_enable_allowed: bool = False
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"AdaptiveMyCycleOptionAllowables: Disable:{self.adaptive_disable_allowed}, Enable:{self.adaptive_enable_allowed}"
