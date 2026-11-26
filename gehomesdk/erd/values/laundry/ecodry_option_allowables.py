from typing import NamedTuple
    
class ErdEcoDryOptionAllowables (NamedTuple):
    ecodry_disable_allowed: bool = False
    ecodry_enable_allowed: bool = False
    raw_value: str | None = None
    
    def stringify(self, **kwargs):
        return f"EcoDryOptionAllowables: Disable:{self.ecodry_disable_allowed}, Enable:{self.ecodry_enable_allowed}"
