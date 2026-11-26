import enum

@enum.unique
class ErdAutofillPitcherState(enum.Enum):
    DISABLED = "00"
    ENABLED = "01"
    NA = "FF"

    def stringify(self, **kwargs) -> str | None:
        if(self == ErdAutofillPitcherState.NA):
            return "N/A"
        return self.name.title()
