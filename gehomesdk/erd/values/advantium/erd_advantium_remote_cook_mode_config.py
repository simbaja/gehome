from typing import List, NamedTuple, Optional
from dataclasses import dataclass
from .advantium_enums import *

@dataclass(repr=True, eq=True)
class ErdAdvantiumRemoteCookModeConfig:
    microwave_staged_time_enable: bool = False 
    microwave_staged_temp_enable: bool = False
    microwave_slow_cook_time_enable: bool = False
    microwave_slow_cook_temp_enable: bool = False
    precision_cook_time_enable: bool = False
    precision_cook_temp_enable: bool = False
    precision_cook_staged_time_enable: bool = False 
    precision_cook_staged_temp_enable: bool = False 
    precision_cook_custom_time_enable: bool = False 
    precision_cook_custom_temp_enable: bool = False
    precision_cook_custom_upper_heater_enable: bool = False
    precision_cook_custom_lower_heater_enable: bool = False
    precision_cook_custom_microwave_enable: bool = False
    precision_cook_custom_convection_enable: bool = False
    warm_enable: bool = False
    warm_time_enable: bool = False
    warm_temp_enable: bool = False 
    proof_enable: bool = False
    proof_time_enable: bool = False 
    proof_temp_enable: bool = False
    toast_enable: bool = False
    toast_time_enable: bool = False 
    toast_temp_enable: bool = False 
    steam_clean_time_enable: bool = False 
    steam_clean_temp_enable: bool = False 
    convection_bake_enable: bool = False 
    convection_bake_time_enable: bool = False 
    convection_bake_temp_enable: bool = False
    broil_enable: bool = False 
    broil_time_enable: bool = False 
    broil_temp_enable: bool = False
    microwave_time_enable: bool = False 
    microwave_temp_enable: bool = False 
    microwave_sensor_time_enable: bool = False 
    microwave_sensor_temp_enable: bool = False 
    raw_value: Optional[str] = None

    def __init__(self, values: Optional[List[int]], raw_value = Optional[str]) -> None:
        self.raw_value = raw_value

        if values == None:
            return

        self.check_convection_bake(values[0])
        self.check_broil(values[1])
        self.check_microwave(values[2])
        self.check_microwave_sensor(values[3])
        self.check_microwave_staged(values[4])
        self.check_microwave_slow_cook(values[5])
        self.check_precision_cook(values[6])
        self.check_precision_cook_staged(values[7])
        self.check_precision_cook_custom(values[8])
        self.check_warm(values[9])
        self.check_proof(values[10])
        self.check_toast(values[11])
        self.check_steam_clean(values[12])
        
    def check_broil(self, value: int):
        self.broil_enable = value & 1 == 1
        self.broil_time_enable = value & 4 == 4
        self.broil_temp_enable = value & 8 == 8

    def check_convection_bake(self, value: int):
        self.convection_bake_enable = value & 1 == 1
        self.convection_bake_time_enable = value & 4 == 4
        self.convection_bake_temp_enable = value & 8 == 8

    def check_microwave(self, value: int):
        self.microwave_time_enable = value & 4 == 4
        self.microwave_temp_enable = value & 8 == 8

    def check_microwave_sensor(self, value: int):
        self.microwave_sensor_time_enable = value & 4 == 4
        self.microwave_sensor_temp_enable = value & 8 == 8

    def check_microwave_staged(self, value: int):
        self.microwave_staged_time_enable = value & 4 == 4
        self.microwave_staged_temp_enable = value & 64 == 64
    
    def check_precision_cook_custom(self, value: int):
        self.precision_cook_custom_time_enable = value & 4 == 4
        self.precision_cook_custom_temp_enable = value & 8 == 8
        self.precision_cook_custom_upper_heater_enable = value & 16 == 16
        self.precision_cook_custom_lower_heater_enable = value & 32 == 32
        self.precision_cook_custom_microwave_enable = value & 64 == 64
        self.precision_cook_custom_convection_enable = value & 128 == 128

    def check_precision_cook_staged(self, value: int):
        self.precision_cook_staged_time_enable = value & 4 == 4
        self.precision_cook_staged_temp_enable = value & 8 == 8

    def check_precision_cook(self, value: int):
        self.precision_cook_time_enable = value & 4 == 4
        self.precision_cook_temp_enable = value & 8 == 8

    def check_proof(self, value: int):
        self.proof_enable = value & 1 == 1
        self.proof_time_enable = value & 4 == 4
        self.proof_temp_enable = value & 8 == 8

    def check_steam_clean(self, value: int):
        self.steam_clean_time_enable = value & 4 == 4
        self.steam_clean_temp_enable = value & 8 == 8

    def check_toast(self, value: int):
        self.toast_enable = value & 1 == 1
        self.toast_time_enable = value & 4 == 4
        self.toast_temp_enable = value & 8 == 8

    def check_warm(self, value: int):
        self.warm_enable = value & 1 == 1
        self.warm_time_enable = value & 4 == 4
        self.warm_temp_enable = value & 8 == 8

    def check_microwave_slow_cook(self, value: int):
        self.microwave_slow_cook_time_enable = value & 4 == 4
        self.microwave_slow_cook_temp_enable = value & 8 == 8

 
