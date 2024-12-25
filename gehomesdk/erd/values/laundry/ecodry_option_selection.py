import enum
from typing import NamedTuple, Optional
    
class ErdEcoDryOptionSelection (NamedTuple):
    option_enabled: bool = False
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"EcoDryOptionSelection: OptionEnabled:{self.option_enabled}"
