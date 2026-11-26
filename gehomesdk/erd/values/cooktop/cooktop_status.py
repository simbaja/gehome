from typing import NamedTuple
from .erd_cooktop_status import ErdCooktopStatus
from .burner import Burner

class CooktopStatus(NamedTuple):
    status: ErdCooktopStatus
    burners: dict
    raw_value: str | None

    @classmethod
    def DEFAULT(cls):
        return cls(ErdCooktopStatus.DASH, {}, None)

    @property
    def left_front(self) -> Burner | None:
        try:
            return self.burners["leftFront"]
        except(KeyError):
            return None

    @property
    def left_rear(self) -> Burner | None:
        try:
            return self.burners["leftRear"]
        except(KeyError):
            return None
    
    @property
    def center_front(self) -> Burner | None:
        try:
            return self.burners["centerFront"]
        except(KeyError):
            return None

    @property
    def center_rear(self) -> Burner | None:
        try:
            return self.burners["centerRear"]
        except(KeyError):
            return None

    @property
    def right_front(self) -> Burner | None:
        try:
            return self.burners["rightFront"]
        except(KeyError):
            return None
    
    @property
    def right_rear(self) -> Burner | None:
        try:
            return self.burners["rightRear"]
        except(KeyError):
            return None

    def boolify(self):
        return self.status == ErdCooktopStatus.BURNERS_ON
