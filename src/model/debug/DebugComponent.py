from abc import ABC
import numpy as np
from helper import SVGHelper
from model.PlanComponent import PlanComponent


class DebugComponent(PlanComponent, ABC):
    def __init__(self, layer:str):
        self.layer = layer
        self.is_debug = True

    def get_svg_style_string(self):
        svg_style_string_list = []
        svg_style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Text', 'fill: #ac9d00', 'font-size: 10pt', 'font-family: monospace', 'text-anchor: middle'))
        svg_style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Line', 'fill: none', 'stroke: #ac9d00', 'stroke-width: 1px'))
        
        return '\n'.join(svg_style_string_list)

