import math

import numpy as np
from svgwriter.PlanType import PlanType
import helper.SVGHelper as SVGHelper
from model.PlanComponent import PlanComponent
from model.Shape import Shape


class Steps(Shape):
    inverted_running_dir:bool = False
    plan_belonging = PlanType.OVERVIEW
    
    def get_svg_string(self, scale_divisor):
        rel_points = self.translate_point_list_to_position(self.points)
        transformed_rel_points = PlanComponent.transform_points_for_plan(rel_points, scale_divisor)

        svg_string_list = []

        step_centroids = []
        
        for i in range(0, int(len(transformed_rel_points)/2)):
            step_point1 = transformed_rel_points[i]
            step_point2 = transformed_rel_points[len(transformed_rel_points)-i-1]

            step_centroids.append((step_point1+step_point2)/2)
            svg_string_list.append(SVGHelper.gen_line_string(step_point1, step_point2, type(self).__name__))

        path_string_adds_list = []
        if not self.inverted_running_dir:
            path_string_adds_list.append(f'marker-start="url(#{type(self).__name__}-Circle)"')
            path_string_adds_list.append(f'marker-end="url(#{type(self).__name__}-Arrowhead)"')
        else:
            path_string_adds_list.append(f'marker-start="url(#{type(self).__name__}-Arrowhead-Inverted)"')
            path_string_adds_list.append(f'marker-end="url(#{type(self).__name__}-Circle)"')
        
        svg_string_list.append(SVGHelper.gen_path_string(step_centroids, False, type(self).__name__, ' '.join(path_string_adds_list)))
        
        return '\n'.join(svg_string_list)
    
    def get_svg_style_string(self):
        style_string_list = []
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}', 'fill: none', 'stroke: black', 'stroke-width: 0.5px'))
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Circle', 'fill: black'))
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Arrowhead', 'fill: black'))
        return '\n'.join(style_string_list)
    
    def get_svg_definition_string(self):
        definition_string_list = [] 
        
        super_svg_definition_string = super().get_svg_definition_string()
        if super_svg_definition_string is not None:
            definition_string_list.append(super_svg_definition_string)

        definition_string = f'<marker id="{type(self).__name__}-Arrowhead" orient="auto" markerWidth="4" markerHeight="4" refX="4" refY="2">'
        definition_string += f'<path class="{type(self).__name__}-Arrowhead" d="M0,0 V4 L4,2 Z" />'
        definition_string += '</marker>'
        definition_string_list.append(definition_string)

        definition_string = f'<marker id="{type(self).__name__}-Arrowhead-Inverted" orient="auto" markerWidth="4" markerHeight="4" refX="0" refY="2">'
        definition_string += f'<path class="{type(self).__name__}-Arrowhead" d="M4,0 V4 L0,2 Z" />'
        definition_string += '</marker>'
        definition_string_list.append(definition_string)

        definition_string = f'<marker id="{type(self).__name__}-Circle" orient="auto" markerWidth="4" markerHeight="4" refX="2" refY="2">'
        definition_string += f'<circle class="{type(self).__name__}-Circle" cx="2" cy="2" r="2" />'
        definition_string += '</marker>'
        definition_string_list.append(definition_string)

        return '\n'.join(definition_string_list)
    
    def validate(self):
        return super().validate()