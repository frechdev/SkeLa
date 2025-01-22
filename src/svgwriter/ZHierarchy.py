from typing import List
from exceptions.NotImplementedException import NotImplementedException
from model.Component import Component
from model.Dimension import Dimension
from model.Furniture import Furniture
from model.ZDimension import ZDimension
from model.debug.Axes import Axes
from model.debug.DebugLabel import DebugLabel
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
    Stairs,
    Steps,
    Opening,
    OpeningArc,
    Label,
    Furniture,
    KNXTemperatureSensor,
    KNXTouchSensor,
    SocketPower,
    SocketData,
    Dimension,
    ZDimension,
    DebugLabel,
    Axes,
]

def sort_by_z_hierarchy(components:List[Component]):
    
    undefined_objects = [obj for obj in components if type(obj) not in z_hierarchy]
    if len(undefined_objects) > 0:
        raise Exception(f"Type {type(undefined_objects[0])} is not implemented in {z_hierarchy=}")
    
    order_map = {cls: index for index, cls in enumerate(z_hierarchy)}

    sorted_components = sorted(
        components,
        key=lambda comp: order_map.get(type(comp))
    )
    
    return sorted_components