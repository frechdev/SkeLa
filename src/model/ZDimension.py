import numpy as np
from exceptions.ValidationError import ValidationError
from helper import SVGHelper
from model.PlanComponent import PlanComponent
from svgwriter.PlanType import PlanType


class ZDimension(PlanComponent):
    lower_height:int = 0
    upper_height:int = 0
    plan_belonging: PlanType = PlanType.HEIGHTS
    font_size = SVGHelper.FontSize.SMALL.value

    def get_svg_style_string(self):
        style_string_list = []
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Text', 'fill: #00a1a1', 'font-family: monospace', 'text-anchor: left'))
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Dot', 'fill: #00a1a1'))
        return '\n'.join(style_string_list) 

    def get_svg_string(self, scale_divisor):
        transformed_position = PlanComponent.transform_point_for_plan(self.position, scale_divisor)        

        text_content_list = []
        text_content_list.append(f'h = {self.lower_height}')
        text_content_list.append(f'H = {self.upper_height}')
        text_content_list.append(f'dh = {self.upper_height-self.lower_height}')
        
        text_position_offset = np.array([0.1, 0])
        text_position = np.add(transformed_position, text_position_offset)
        
        svg_string_list = []
        svg_string_list.append(f'<text class="{type(self).__name__}-Text" font-size="{self.font_size}"  x="{text_position[0]}" y="{text_position[1]}">')
        
        dy = 0
        for text_content in text_content_list:
            svg_string_list.append(f'<tspan x="{text_position[0]}" dy="{dy}">{text_content}</tspan>')
            dy = self.font_size
        
        svg_string_list.append(f'</text>')
        svg_string_list.append(SVGHelper.gen_circle_string(transformed_position, 0.1, f'{type(self).__name__}-Dot'))
        
        
        return '\n'.join(svg_string_list)
