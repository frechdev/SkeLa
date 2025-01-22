from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Tuple

import numpy as np
from exceptions.NotImplementedException import NotImplementedException
from helper import PlanCalculations
from model.Component import Component


class PlanComponent(Component, ABC):
    position: np.ndarray = np.zeros(2, int)
    
    @abstractmethod
    def get_svg_string(self, scale_divisor:int) -> str:
        raise NotImplementedException(self.get_svg_string.__name__, type(self).__name__)

    @classmethod
    def transform_point_for_plan(cls, point:np.ndarray, scale_divisor:int) -> np.ndarray:
        return PlanCalculations.scale_point_for_plan(PlanCalculations.invert_y(point), scale_divisor)

    @classmethod        
    def transform_points_for_plan(cls, points:List[np.ndarray], scale_divisor:int) -> List[np.ndarray]:
        transformed_points = list(map(lambda n: PlanComponent.transform_point_for_plan(n, scale_divisor), points))
        return transformed_points

    def create_debug_components(self) -> List[DebugComponent]:
        pass

    def translate_point_to_position(self, point:np.ndarray) -> np.ndarray:
        return PlanCalculations.ref_point(point, self.position)
    
    def translate_point_list_to_position(self, points:List[np.ndarray]) -> List[np.ndarray]:
        return list(map(lambda n: PlanCalculations.ref_point(n, self.position), points))
    
    
        
