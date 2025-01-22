from abc import ABC, abstractmethod
from exceptions.NotImplementedException import NotImplementedException
from model.DSLBaseClass import DSLBaseClass
from svgwriter.PlanType import PlanType


class Component(DSLBaseClass, ABC):
    layer: str = None
    is_hidden: bool = False
    is_debug: bool = False
    plan_belonging: PlanType = PlanType.OVERVIEW | PlanType.XY_DIMENSIONS | PlanType.HEIGHTS | PlanType.FURNITURE | PlanType.ELECTRICAL
    
    @abstractmethod
    def get_svg_style_string(self) -> str:
        raise NotImplementedException(self.get_svg_style_string.__name__, type(self).__name__)
    
    def get_svg_definition_string(self) -> str:
        pass        
    
    def validate(self):
        return super().validate()