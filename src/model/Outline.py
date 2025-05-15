from numpy import add
import helper.SVGHelper as SVGHelper
from model.Shape import Shape


class Outline(Shape):
            
    def get_svg_style_string(self):
        return SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: #2b2b2b', 'stroke: black', 'stroke-width: 1px')
    
    def validate(self):
        return super().validate()
    
