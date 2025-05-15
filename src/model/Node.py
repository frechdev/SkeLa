from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Tuple
import numpy as np
from exceptions.NotImplementedException import NotImplementedException
from exceptions.ValidationError import ValidationError
from helper import PlanCalculations
from model.PlanComponent import PlanComponent
from model.ReferenceableComponent import Anchor, ReferenceableComponent

    

class Node(ReferenceableComponent, ABC):
    anchor:Anchor
    rotation:int = 0
    _original_width:int
    _original_height:int


    def get_global_boundry(self) -> Tuple[np.ndarray, np.ndarray]:
        return super().get_global_boundry()

    def get_global_anchor_position(self, anchor:Anchor):
        relative_boundry_vector = np.array([self._original_width, self._original_height])
        
        non_rotated_relative_anchor_position = (np.array(anchor.value) - np.array(self.anchor.value)) * relative_boundry_vector
        
        non_rotated_relative_anchor_position = PlanCalculations.invert_y(non_rotated_relative_anchor_position)
        
        rotation_mat = PlanCalculations.rotation_matrix(self.rotation)
        rotated_anchor_position = np.dot(non_rotated_relative_anchor_position, rotation_mat)

        global_anchor_position = self.position + rotated_anchor_position
        return global_anchor_position
    
    def get_svg_string(self, scale_divisor):
        non_rotated_relative_anchor_position = np.array(self.anchor.value) * np.array([self._original_width, self._original_height])
                
        transformed_position = PlanComponent.transform_point_for_plan(self.position, scale_divisor)
        
        svg_string = f'<use href="#{type(self).__name__}-Node" transform="translate({transformed_position[0]}cm {transformed_position[1]}cm) rotate({self.rotation}) scale({1/scale_divisor}) translate({-non_rotated_relative_anchor_position[0]}cm {-non_rotated_relative_anchor_position[1]}cm)"/>'
        
        return svg_string

    def validate(self):
        if not isinstance(self.rotation, int):
            raise ValidationError(f"Attribute 'rotation' must be an integer number.")

        
        return super().validate()