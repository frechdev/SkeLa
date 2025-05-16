from typing import List
import numpy as np
from exceptions.ValidationError import ValidationError
from helper import PlanCalculations, SVGHelper
from model.PlanComponent import PlanComponent
from model.ReferenceableComponent import Anchor
from model.Room import Room
from svgwriter.PlanType import PlanType


class AreaDimension(PlanComponent):
    plan_belonging: PlanType = PlanType.XY_DIMENSIONS
    area:float
    
    def __init__(self, room:Room):
        self.area = PlanCalculations.calc_polygon_area(room.points)
        self.layer = room.layer
        self.position = room.get_global_anchor_position(Anchor.CENTER)
    
    def get_svg_style_string(self):
        style_string_list = []
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Text', 'fill: #00a1a1', 'font-family: monospace', 'text-anchor: middle'))
        return '\n'.join(style_string_list) 

    def get_svg_string(self, scale_divisor):
        transformed_position = PlanComponent.transform_point_for_plan(self.position, scale_divisor)        

        area_in_qm = round(self.area / 10000, 2)
        
        return SVGHelper.gen_text_string(transformed_position, SVGHelper.FontSize.NORMAL, f'{area_in_qm}qm', f'{type(self).__name__}-Text')
        
