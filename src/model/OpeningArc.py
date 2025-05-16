import math

import numpy as np
from model.PlanComponent import PlanComponent
from svgwriter.PlanType import PlanType
import helper.SVGHelper as SVGHelper
from model.Shape import Shape


class OpeningArc(Shape):
    plan_belonging: PlanType = PlanType.OVERVIEW | PlanType.FURNITURE

    def get_svg_string(self, scale_divisor):
        rel_points = self.translate_point_list_to_position(self.points)
        transformed_rel_points = PlanComponent.transform_points_for_plan(rel_points, scale_divisor)
        
        radius = np.linalg.norm(transformed_rel_points[1]-transformed_rel_points[0])

        v1 = transformed_rel_points[1]-transformed_rel_points[0]
        v2 = transformed_rel_points[2]-transformed_rel_points[0]
        angle = math.atan2(v2[1], v2[0]) - math.atan2(v1[1], v1[0])
        if (angle < 0): angle += 2*math.pi
        if (angle < math.pi):
            arc_dir = 1
        else:
            arc_dir = 0

        svg_string = f'<path class="{type(self).__name__}" d="'
        svg_string += f'M{transformed_rel_points[0][0]} {transformed_rel_points[0][1]} '
        svg_string += f'L{transformed_rel_points[1][0]} {transformed_rel_points[1][1]} '
        svg_string += f'A{radius} {radius} 0 0 {arc_dir} {transformed_rel_points[2][0]} {transformed_rel_points[2][1]} '
        svg_string += 'Z" />'
        
        return svg_string
    
    def get_svg_style_string(self):
        return SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: #b3b3b3', 'stroke: black', f'stroke-width: {SVGHelper.StrokeWidth.NORMAL.value}')
    
    def validate(self):
        return super().validate()