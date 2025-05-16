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
        svg_style_string_list = []
        svg_style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-BG', 'fill: white', 'font-family: monospace', 'font-weight: bold'))
        svg_style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-FG', 'fill: black', 'font-family: monospace'))
        return '\n'.join(svg_style_string_list)

    def get_svg_string(self, scale_divisor):
        transformed_position = PlanComponent.transform_point_for_plan(self.position, scale_divisor)        

        svg_string_list = []
        svg_string_list.append(SVGHelper.gen_text_string(transformed_position, SVGHelper.FontSize.NORMAL, self.content, f'{type(self).__name__}-BG'))
        svg_string_list.append(SVGHelper.gen_text_string(transformed_position, SVGHelper.FontSize.NORMAL, self.content, f'{type(self).__name__}-FG'))

        return '\n'.join(svg_string_list)
