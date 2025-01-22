from enum import Flag, auto


class PlanType(Flag):
    OVERVIEW = auto()
    XY_DIMENSIONS = auto()
    HEIGHTS = auto()
    FURNITURE = auto()
    ELECTRICAL = auto()
    
clear_name_mapping = {
    PlanType.OVERVIEW: "Übersicht",
    PlanType.XY_DIMENSIONS: "XY-Dimensionen",
    PlanType.HEIGHTS: "Höhenprofil",
    PlanType.FURNITURE: "Einrichtung",
    PlanType.ELECTRICAL: "Elektroinstallation",
}

def get_clear_name(flag):
    return clear_name_mapping.get(flag, f"Unbekannt ({flag.name})")

