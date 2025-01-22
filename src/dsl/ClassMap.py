from model.Dimension import Dimension
from model.Furniture import Furniture
from model.Label import Label
from model.MetaInformation import MetaInformation
from model.Opening import Opening
from model.OpeningArc import OpeningArc
from model.Outline import Outline
from model.Room import Room
from model.Settings import Settings
from model.Stairs import Stairs
from model.Steps import Steps
from model.ZDimension import ZDimension
from model.electrical_nodes.KNXTouchSensor import KNXTouchSensor
from model.electrical_nodes.KNXTemperatureSensor import KNXTemperatureSensor
from model.electrical_nodes.SocketPower import SocketPower
from model.electrical_nodes.SocketData import SocketData


class_map = {
        "SETTINGS": Settings,
        "META_INFORMATION": MetaInformation,
        "OUTLINE": Outline,
        "ROOM": Room,
        "OPENING": Opening,
        "OPENING_ARC": OpeningArc,
        "STAIRS": Stairs,
        "STEPS": Steps,
        "LABEL": Label,
        "DIM": Dimension,
        "ZDIM": ZDimension,
        "FURNITURE": Furniture,
        "KNX_TOUCH_SENSOR": KNXTouchSensor,
        "KNX_TEMPERATURE_SENSOR": KNXTemperatureSensor,
        "SOCKET_POWER": SocketPower,
        "SOCKET_DATA": SocketData,
    }
