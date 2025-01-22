import numpy as np
from exceptions.ValidationError import ValidationError
from helper import SVGHelper
from model.PlanComponent import PlanComponent
from model.ReferenceableComponent import Anchor, ReferenceableComponent
from model.debug.DebugComponent import DebugComponent
from svgwriter.PlanType import PlanType


class DebugLabel(DebugComponent):
    content:str

    def __init__(self, layer:str, position:np.ndarray, content:str, plan_belonging:PlanType):
        super().__init__(layer)
        
        self.position = position
        self.content = content
        self.plan_belonging = plan_belonging
    
    def get_svg_string(self, scale_divisor):
        transformed_position = PlanComponent.transform_point_for_plan(self.position, scale_divisor)        

        svg_string = SVGHelper.gen_text_string(transformed_position, self.content, f'{type(self).__name__}-Text')

        return svg_string
