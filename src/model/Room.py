import helper.SVGHelper as SVGHelper
from model.Shape import Shape


class Room(Shape):
    def get_svg_style_string(self):
        return SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: #d9d9d9', 'stroke: black', f'stroke-width: {SVGHelper.StrokeWidth.THICK.value}')
    
    def validate(self):
        return super().validate()