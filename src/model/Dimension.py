import numpy as np
from exceptions.ValidationError import ValidationError
from helper import PlanCalculations
import helper.SVGHelper as SVGHelper
from exceptions.MissingAttributeError import MissingAttributeError
from model.PlanComponent import PlanComponent
from svgwriter.PlanType import PlanType


class Dimension(PlanComponent):
    dir:str
    offset:int = 0
    is_derived:bool = False
    reference:np.ndarray = None
    point1:np.ndarray
    point2:np.ndarray
    plan_belonging: PlanType = PlanType.XY_DIMENSIONS
    
    def get_svg_style_string(self):
        style_string_list = []
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Text', 'fill: #a10000', 'font-size: 7pt', 'font-family: monospace', 'text-anchor: middle'))
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Line', 'fill: none', 'stroke: black', 'stroke-width: 0.5px'))
        return '\n'.join(style_string_list) 
    
    def get_svg_string(self, scale_divisor):

        transformed_point1 = PlanCalculations.scale_point_for_plan(PlanCalculations.invert_y(self.point1), scale_divisor)
        transformed_point2 = PlanCalculations.scale_point_for_plan(PlanCalculations.invert_y(self.point2), scale_divisor)

        transformed_reference:np.array
        if self.reference is None:
            transformed_reference = transformed_point1
        else:
            transformed_reference = PlanCalculations.scale_point_for_plan(PlanCalculations.invert_y(self.reference), scale_divisor)
        
        dimension_text:str
        text_offset_x:int
        text_offset_y:int
        text_rotation:int
        dim_line_anchor1:np.array
        dim_line_anchor2:np.array
        match self.dir:
            case "x":
                dimension_text = int(abs(self.point2[0]-self.point1[0]))
                                    
                if self.is_derived:
                    dimension_text = f'({dimension_text})'

                dim_line_anchor1 = np.array([transformed_point1[0], transformed_reference[1]])
                dim_line_anchor2 = np.array([transformed_point2[0], transformed_reference[1]])
                
                if self.point2[0]>self.point1[0]:
                    text_offset_y = -2
                    dim_line_anchor1 = dim_line_anchor1 - np.array([0, self.offset])
                    dim_line_anchor2 = dim_line_anchor2 - np.array([0, self.offset])
                else:
                    text_offset_y = 9
                    dim_line_anchor1 = dim_line_anchor1 + np.array([0, self.offset])
                    dim_line_anchor2 = dim_line_anchor2 + np.array([0, self.offset])
                
                text_offset_x = 0
                text_rotation = 0

            case "y":
                dimension_text = int(abs(self.point2[1]-self.point1[1]))
                                    
                if self.is_derived:
                    dimension_text = f'({dimension_text})'

                dim_line_anchor1 = np.array([transformed_reference[0], transformed_point1[1]])
                dim_line_anchor2 = np.array([transformed_reference[0], transformed_point2[1]])
                
                if self.point2[1]>self.point1[1]:
                    text_offset_x = -2
                    dim_line_anchor1 = dim_line_anchor1 - np.array([self.offset, 0])
                    dim_line_anchor2 = dim_line_anchor2 - np.array([self.offset, 0])
                else:
                    text_offset_x = 9
                    dim_line_anchor1 = dim_line_anchor1 + np.array([self.offset, 0])
                    dim_line_anchor2 = dim_line_anchor2 + np.array([self.offset, 0])
                
                text_offset_y = 0
                text_rotation = -90

            case _:
                raise ValueError(f"direction must be 'x' or 'y'")
                    
        dim_line_center = (dim_line_anchor1 + dim_line_anchor2)/2
        transform_x = dim_line_center[0] + text_offset_x
        transform_y = dim_line_center[1] + text_offset_y
        transform_rot = text_rotation

        svg_string_list = []
        svg_string_list.append(f'<text class="{type(self).__name__}-Text" transform="translate({transform_x} {transform_y}) rotate({transform_rot})">{dimension_text}</text>')

        if (self.offset != 0):
            line1_x1, line1_y1 = transformed_point1
            line1_x2, line1_y2 = dim_line_anchor1
            line2_x1, line2_y1 = transformed_point2
            line2_x2, line2_y2 = dim_line_anchor2
            line3_x1, line3_y1 = dim_line_anchor1
            line3_x2, line3_y2 = dim_line_anchor2

            svg_string_list.append(f'<line class="{type(self).__name__}-Line" x1="{line1_x1}" y1="{line1_y1}" x2="{line1_x2}" y2="{line1_y2}" />')
            svg_string_list.append(f'<line class="{type(self).__name__}-Line" x1="{line2_x1}" y1="{line2_y1}" x2="{line2_x2}" y2="{line2_y2}" />')
            svg_string_list.append(f'<line class="{type(self).__name__}-Line" x1="{line3_x1}" y1="{line3_y1}" x2="{line3_x2}" y2="{line3_y2}" />')
        
        
        return '\n'.join(svg_string_list)

    
    def validate(self):
        if not self.dir:
            raise MissingAttributeError('direction', __name__)

        if self.dir not in {"x", "y"}:
            raise ValidationError("Value for attribut 'direction' must be 'x' or 'y'.")
        
        if not isinstance(self.point1, np.ndarray):
            raise ValidationError("Value for attribut 'point1' must be a point.")

        if not isinstance(self.point2, np.ndarray):
            raise ValidationError("Value for attribut 'point2' must be a point.")
        
        if not np.array_equal(self.position, np.zeros(2, int)):
            raise ValidationError(f"Attribute 'position' ist not supported for {__name__}")
        
        return super().validate()
        

