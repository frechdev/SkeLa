from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Tuple
import numpy as np
from exceptions.NotImplementedException import NotImplementedException
from helper import PlanCalculations
from model.ReferenceableComponent import Anchor, ReferenceableComponent

    

class Node(ReferenceableComponent, ABC):
    anchor:Anchor
    
    def get_global_position(self) -> np.ndarray:
        base_anchor_offset = np.array(self.anchor.value) * np.array(self.get_size())
        global_position = self.position - base_anchor_offset

        return global_position
        
    def get_boundry(self) -> Tuple[np.ndarray, np.ndarray]:
        width, height = self.get_size()
        
        x_min = self.get_global_position()[0]
        x_max = x_min + width
        
        y_min = self.get_global_position()[1]
        y_max = y_min + height

        return np.array([x_min, y_min]), np.array([x_max, y_max])

    @abstractmethod
    def get_size(self) -> Tuple[int, int]:
        raise NotImplementedException(self.get_size.__name__, type(self).__name__)
