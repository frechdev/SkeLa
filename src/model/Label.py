import numpy as np
from exceptions.ValidationError import ValidationError
from helper import SVGHelper
from model.PlanComponent import PlanComponent
from svgwriter.PlanType import PlanType


class Label(PlanComponent):
    content:str
    plan_belonging: PlanType = PlanType.OVERVIEW

    def validate(self):
        if self.content is None:
            raise ValidationError("Value for attribut 'content' must be set.")
        
        return super().validate()

    def get_svg_style_string(self):
        return SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: black', 'font-size: 9pt', 'font-family: monospace', 'font-weight: bold')

    def get_svg_string(self, scale_divisor):
        transformed_position = PlanComponent.transform_point_for_plan(self.position, scale_divisor)        

        return SVGHelper.gen_text_string(transformed_position, self.content, type(self).__name__)
