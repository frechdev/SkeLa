from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple

import numpy as np

from exceptions.MissingAttributeError import MissingAttributeError
from exceptions.NotImplementedException import NotImplementedException
from model.PlanComponent import PlanComponent
from model.Component import Component

class Anchor(Enum):
    CENTER = (0.5, 0.5)
    TOP = (0.5, 0.0)
    BOTTOM = (0.5, 1.0)
    LEFT = (0.0, 0.5)
    RIGHT = (1.0, 0.5)
    TOP_LEFT = (0.0, 0.0)
    TOP_RIGHT = (1.0, 0.0)
    BOTTOM_LEFT = (0.0, 1.0)
    BOTTOM_RIGHT = (1.0, 1.0)

class ReferenceableComponent(PlanComponent, ABC):
    id: str
        
    @abstractmethod
    def get_global_position(self) -> np.ndarray:
        raise NotImplementedException(self.get_global_position.__name__, type(self).__name__)
    
    @abstractmethod
    def get_boundry(self) -> Tuple[np.ndarray, np.ndarray]:
        raise NotImplementedException(self.get_boundry.__name__, type(self).__name__)

    def get_global_anchor_position(self, anchor:Anchor) -> np.ndarray:
        min_coords, max_coords = self.get_boundry()

        boundry_vector = max_coords - min_coords
        
        global_anchor_position = (np.array(anchor.value) * boundry_vector) + min_coords
        
        return global_anchor_position
        
    def get_relative_anchor_position(self, anchor:Anchor) -> np.ndarray:
        relative_anchor_position = self.get_global_anchor_position(anchor) - self.get_global_position()
        
        return relative_anchor_position

    def validate(self):
        if not self.id:
            raise MissingAttributeError('id', __name__)

        return super().validate()
    


