import enum

@enum.unique
class ErdOvenLightLevel(enum.Enum):
    OFF = 0
    HIGH = 1
    DIM = 2
    NOT_AVAILABLE = 255

    def boolify(self) -> bool | None:
        return self != ErdOvenLightLevel.OFF

    def stringify(self, **kwargs):
        return self.name.title()