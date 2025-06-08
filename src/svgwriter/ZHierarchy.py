from typing import List, Type
from exceptions.NotImplementedException import NotImplementedException
from model.AreaDimension import AreaDimension
from model.Component import Component
from model.Dimension import Dimension
from model.Furniture import Furniture
from model.Slope import Slope
from model.ZDimension import ZDimension
from model.debug.Axes import Axes
from model.debug.DebugLabel import DebugLabel
from model.electrical_nodes.ElectricalNode import ElectricalNode
from model.electrical_nodes.KNXBusInterface import KNXBusInterface
from model.electrical_nodes.KNXTemperatureSensor import KNXTemperatureSensor
from model.electrical_nodes.KNXTouchSensor import KNXTouchSensor
from model.electrical_nodes.SocketData import SocketData
from model.electrical_nodes.SocketPower import SocketPower
from model.Label import Label
from model.Opening import Opening
from model.OpeningArc import OpeningArc
from model.Outline import Outline
from model.Room import Room
from model.Stairs import Stairs
from model.Steps import Steps


z_hierarchy = [
    Outline,
    Room,
    Slope,
    Stairs,
    Steps,
    Opening,
    OpeningArc,
    Label,
    Furniture,
    ElectricalNode,
    AreaDimension,
    Dimension,
    ZDimension,
    DebugLabel,
    Axes,
]

def sort_by_z_hierarchy(components:List[Component]):
    def get_z_order(cls: Type) -> int:
        """Find the position of the class or its nearest parent in z_hierarchy."""
        for index, z_cls in enumerate(z_hierarchy):
            if issubclass(cls, z_cls):  # Check if cls is a subclass of z_cls
                return index
        raise NotImplementedError(f"Type {cls} is not implemented in {z_hierarchy=}")

    sorted_components = sorted(
        components,
        key=lambda comp: get_z_order(type(comp))
    )
    
    return sorted_components