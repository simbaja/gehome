import enum
from typing import Optional

@enum.unique
class ErdAutofillPitcherState(enum.Enum):
    DISABLED = "00"
    ENABLED = "01"
    NA = "FF"

    def stringify(self, **kwargs) -> Optional[str]:
        if(self == ErdAutofillPitcherState.NA):
            return "N/A"
        return self.name.title()
