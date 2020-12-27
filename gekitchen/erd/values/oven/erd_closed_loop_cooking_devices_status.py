#WIP

import enum

#0x5771
#0x5772
#0x5773
#0x5774
#0x5775
#0x5776
#0x5777

class ErdCloseLoopCookingDevicesStatus:
    class CookingDeviceType(enum.Enum):
        DEFAULT = "Default"
        HESTANT_CUE_PAN = "HestanCuePan"
        HESTANT_CUE_POT = "HestanCuePot"
        PARAGON_SENSOR = "Paragon"
        POPUP_SENSOR = "PopupSensor"

    _CODE_MAPPING = {
        "0x5771": "0x5778",
        "0x5772": "0x5779",
        "0x5773": "0x577a",
        "0x5774": "0x577b",
        "0x5775": "0x577c",
        "0x5776": "0x577d",
        "0x5777": "0x577e"
    }
    _y0 = 100
    _z0 = 450

    def __init__(self, value: str, code: str):
        self.code = ErdCloseLoopCookingDevicesStatus._CODE_MAPPING[code]
        self.t0 = -1
        self.u0 = -1

        if not value:
            self.status = "NoData"
            self.device_type = self.CookingDeviceType.DEFAULT
            self.r0 = 0
        try:
            self.device_type = self._initialize_device_type(value)
            self.r0 = int(value[2,4], 16) #TODO: based on the original logic, this needs error handling
            self.status = value[4,8]
            if len(value) >= 16:
                self.t0 = int(value[8:12], 16)
                self.u0 = int(value[12:16], 16)
            elif self.device_type == self.CookingDeviceType.POPUP_SENSOR:
                self.t0 = ErdCloseLoopCookingDevicesStatus.y0
                self.u0 = ErdCloseLoopCookingDevicesStatus.z0
                pass            
        except:
            self.device_type = self.CookingDeviceType.DEFAULT
            self.r0 = 0
                    
    def _initialize_device_type(self, value: str):
        try:
            return {
                "00": self.device_type.POPUP_SENSOR,
                "01": self.device_type.PARAGON_SENSOR,
                "02": self.device_type.HESTANT_CUE_PAN,
                "03": self.device_type.HESTANT_CUE_POT
            }[value[:2]]
        except:
            return self.device_type.DEFAULT

