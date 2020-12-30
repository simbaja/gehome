from ..primitives import ErdReadOnlyStringConverter

class CycleNameConverter(ErdReadOnlyStringConverter):
    def erd_decode(self, value: str) -> str:
        name = super().erd_decode(value)
        if name.startswith("Autosense"):
            name = "Autosense"

        return name  
