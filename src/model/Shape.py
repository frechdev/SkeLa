from abc import ABC, abstractmethod
from typing import List, Tuple
import numpy as np
from exceptions.NotImplementedException import NotImplementedException
from exceptions.ValidationError import ValidationError
from helper import SVGHelper
from helper import PlanCalculations
from model.Component import Component
from model.PlanComponent import PlanComponent
from model.ReferenceableComponent import Anchor, ReferenceableComponent
from model.debug.DebugLabel import DebugLabel


class Shape(ReferenceableComponent, ABC):
    points: List[np.ndarray]

    def create_debug_components(self):
        debug_components = []

        if super().create_debug_components():
            debug_components.extend(super().create_debug_components())

        debug_components.append(DebugLabel(self.layer, self.get_global_anchor_position(Anchor.CENTER), self.id, self.plan_belonging))

        for i in range(len(self.points)):
            translated_point = self.translate_point_to_position(self.points[i])
            debug_components.append(DebugLabel(self.layer, translated_point, f'{i+1}', self.plan_belonging))

        return debug_components

    def get_global_boundry(self) -> Tuple[np.ndarray, np.ndarray]:
        translated_points = self.translate_point_list_to_position(self.points)
        
        translated_points_array = np.array(translated_points)
        min_coords = translated_points_array.min(axis=0)
        max_coords = translated_points_array.max(axis=0)

        return min_coords, max_coords
    
    def get_global_anchor_position(self, anchor:Anchor) -> np.ndarray:
        min_coords, max_coords = self.get_global_boundry()

        boundry_vector = max_coords - min_coords
        
        global_anchor_position = (np.array(anchor.value) * boundry_vector) + min_coords
        
        return global_anchor_position

    def get_svg_string(self, scale_divisor:int) -> str:
        rel_points = self.translate_point_list_to_position(self.points)
             
        return SVGHelper.gen_path_string(PlanComponent.transform_points_for_plan(rel_points, scale_divisor), True, f'{type(self).__name__}')

    def validate(self):
        if len(self.points) < 2:
            raise ValidationError(f"Number of points for a '{__name__}' must be at least 2.")
        
        return super().validate()
    