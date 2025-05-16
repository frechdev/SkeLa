from typing import List
import numpy as np
from helper import SVGHelper
from model.PlanComponent import PlanComponent
from model.debug.DebugComponent import DebugComponent


class Axes(DebugComponent):    
    def __init__(self):
        super().__init__(None)
            
    def get_svg_string(self, scale_divisor):
        
        transformed_position = PlanComponent.transform_point_for_plan(self.position, scale_divisor)        

        pnts:List[np.ndarray] = [
            transformed_position + np.array([0, -50]),
            transformed_position + np.array([0, 0]),
            transformed_position + np.array([50, 0]),
        ]
        
        svg_string_list = []
        svg_string_list.append(SVGHelper.gen_path_string(pnts, False, f'{type(self).__name__}-Line'))
        svg_string_list.append(SVGHelper.gen_text_string(pnts[0], SVGHelper.FontSize.NORMAL, 'x', f'{type(self).__name__}-Text', 'text-anchor="end"'))
        svg_string_list.append(SVGHelper.gen_text_string(pnts[2] + np.array([5, 5]), SVGHelper.FontSize.NORMAL, 'y', f'{type(self).__name__}-Text'))
        
        return '\n'.join(svg_string_list)
