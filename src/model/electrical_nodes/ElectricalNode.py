from model.Node import Node
from model.PlanComponent import PlanComponent
from svgwriter.PlanType import PlanType


class ElectricalNode(Node):
    rotation:int = 0
    plan_belonging: PlanType = PlanType.ELECTRICAL
    
    def get_svg_string(self, scale_divisor):
        relative_anchor_position = self.get_relative_anchor_position(self.anchor)
        anchored_position = self.position + relative_anchor_position
        
        transformed_anchored_position = PlanComponent.transform_point_for_plan(anchored_position, scale_divisor)
        
        svg_string = f'<use href="#{type(self).__name__}-Symbol" transform="rotate({self.rotation} {relative_anchor_position[0]} {relative_anchor_position[1]})" x="{transformed_anchored_position[0]}" y="{transformed_anchored_position[1]}"/>'
        
        return svg_string

    def get_svg_style_string(self):
        pass