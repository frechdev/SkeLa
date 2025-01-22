import helper.SVGHelper as SVGHelper
from model.Shape import Shape


class Opening(Shape):
    def get_svg_style_string(self):
        return SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: #b3b3b3', 'stroke: black', 'stroke-width: 0.5px')
    
    def validate(self):
        return super().validate()