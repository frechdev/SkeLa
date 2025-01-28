import helper.SVGHelper as SVGHelper
from model.PlanComponent import PlanComponent
from model.ReferenceableComponent import Anchor
from model.Shape import Shape
from svgwriter.PlanType import PlanType


class Furniture(Shape):
    label:str = ''
    plan_belonging: PlanType = PlanType.FURNITURE

    def get_svg_string(self, scale_divisor:int):  
        svg_string_list = [super().get_svg_string(scale_divisor)]
        
        center = self.get_global_anchor_position(Anchor.CENTER)
        transformed_center = PlanComponent.transform_point_for_plan(center, scale_divisor)
        
        svg_string_list.append(SVGHelper.gen_text_string(transformed_center, self.label, f'{type(self).__name__}-Text'))

        return '\n'.join(svg_string_list)
    
    def get_svg_style_string(self):
        svg_style_string_list = []
        svg_style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: white', 'stroke: black', 'stroke-width: 1px'))
        svg_style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Text', 'font-size: 9pt', 'font-family: monospace', 'font-weight: bold', 'text-anchor: middle'))

        return '\n'.join(svg_style_string_list)
    
    def validate(self):
        return super().validate()