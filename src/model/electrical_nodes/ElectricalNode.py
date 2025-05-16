from model.Node import Node
from model.PlanComponent import PlanComponent
from model.ReferenceableComponent import Anchor
from svgwriter.PlanType import PlanType


class ElectricalNode(Node):
    anchor:Anchor = Anchor.LEFT
    plan_belonging: PlanType = PlanType.ELECTRICAL
        
    def get_svg_style_string(self):
        pass