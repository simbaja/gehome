from ..abstract import ErdReadOnlyConverter
from ...values.fridge import ErdAutofillPitcherState

class ErdAutofillPitcherStateConverter(ErdReadOnlyConverter[ErdAutofillPitcherState]):
    def erd_decode(self, value: str) -> ErdAutofillPitcherState:
        try:
            return ErdAutofillPitcherState(value)
        except ValueError:
            return ErdAutofillPitcherState.NA
