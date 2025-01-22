from numpy import add
from helper.PlanCalculations import cm_to_dots, invert_y, invert_y_list, ref_point_list, scale_point_list_for_plan
import helper.SVGHelper as SVGHelper
from model.Shape import Shape


class Outline(Shape):
            
    def get_svg_style_string(self):
        return SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: #2b2b2b', 'stroke: black', 'stroke-width: 1px')
    
    def validate(self):
        return super().validate()
    
