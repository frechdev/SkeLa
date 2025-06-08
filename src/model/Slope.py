import helper.SVGHelper as SVGHelper
from model.Shape import Shape


class Slope(Shape):
    def get_svg_style_string(self):
        return SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: #b3b3b3', 'stroke: black', f'stroke-width: {SVGHelper.StrokeWidth.THIN.value}')
    
    def validate(self):
        return super().validate()