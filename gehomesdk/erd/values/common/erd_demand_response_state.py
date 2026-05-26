import enum


@enum.unique
class ErdDemandResponseState(enum.Enum):
    NOT_AVAILABLE = 255
    NOT_IN_DEMAND_RESPONSE = 0
    IN_DEMAND_RESPONSE = 1
    TEMPORARY_LOAD_REDUCTION = 2

    def stringify(self, **kwargs):
        return self.name.replace("_", " ").title()
