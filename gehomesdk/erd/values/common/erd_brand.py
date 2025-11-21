import enum
from typing import Optional

@enum.unique
class ErdBrand(enum.Enum):
    UNKNOWN = ""
    NOT_DEFINED = "00"
    GEA = "01"
    HEIER = "02"
    MABE = "03"
    FISHER_PAYKEL = "04"
    GE = "05"
    GE_PROFILE = "06"
    GE_CAFE = "07"
    GE_MONOGRAM = "08"
    HOTPOINT = "09"
    HEIER_FPA = "0A"
    ADORA = "0B"
    ALLIED = "0C"
    LENNOX = "0D"

    def stringify(self, **kwargs) -> Optional[str]:
        try:
            return ERD_BRAND_NAME_MAP[self]
        except:
            return ERD_BRAND_NAME_MAP[ErdBrand.UNKNOWN]

ERD_BRAND_NAME_MAP = {
    ErdBrand.UNKNOWN: "Unknown",
    ErdBrand.NOT_DEFINED: "Not Defined",
    ErdBrand.GEA: "GE Appliances",
    ErdBrand.HEIER: "Haier",
    ErdBrand.MABE: "Mabe",
    ErdBrand.FISHER_PAYKEL: "Fisher & Paykel",
    ErdBrand.GE: "GE",
    ErdBrand.GE_PROFILE: "GE Profile",
    ErdBrand.GE_CAFE: "Café",
    ErdBrand.GE_MONOGRAM: "Monogram",
    ErdBrand.HOTPOINT: "Hotpoint",
    ErdBrand.HEIER_FPA: "Fisher & Paykel",
    ErdBrand.ADORA: "Adora",
    ErdBrand.ALLIED: "Allied",
    ErdBrand.LENNOX: "Lennox",
}