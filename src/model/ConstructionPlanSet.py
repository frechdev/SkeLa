from datetime import date
from typing import List
import numpy as np
from helper import PlanCalculations
import helper.ConsolePrinter as cp
from exceptions import NotImplementedException
from exceptions.InputError import InputError
from model.Component import Component
from model.MetaInformation import MetaInformation
from model.ReferenceableComponent import Anchor, ReferenceableComponent
from model.Settings import Settings
from model.Shape import Shape
from model.debug.Axes import Axes


class ConstructionPlanSet:
    component_list:List[Component] = list()
    settings: Settings
    
    def __init__(self):
        self.component_list.append(MetaInformation(title = 'Datum', content = date.today().strftime("%d.%m.%Y")))
        self.component_list.append(Axes())
        
    def get_coordinates_of_point(self, identifier:str, anchor_str:str) -> np.ndarray:
        referenceable_components:list[ReferenceableComponent] = list(filter(lambda n: (isinstance(n, ReferenceableComponent)), self.component_list))
        referenceable_components_by_id:list[ReferenceableComponent] = list(filter(lambda n: n.id == identifier, referenceable_components))
        
        if len(referenceable_components_by_id) < 1:
            raise InputError(f"No component with id: '{identifier}' found!")

        if len(referenceable_components_by_id) > 1:
            raise InputError(f"More then one component with id: '{identifier}' found!")
        
        referenced_component = referenceable_components_by_id[0]
        
        if anchor_str.isdigit():
            if isinstance(referenced_component, Shape):
                anchor = int(anchor_str)
                return PlanCalculations.ref_point(referenced_component.points[anchor-1], referenced_component.position)

        if anchor_str in Anchor.__members__:
            if isinstance(referenced_component, ReferenceableComponent):
                anchor:Anchor = Anchor[anchor_str]
                
                global_anchor_position = referenced_component.get_global_anchor_position(anchor)
                
                
                return global_anchor_position

        raise NotImplementedException()

    
    def get_layers(self):
        layers = set(filter(lambda n: n is not None, map(lambda n: n.layer, self.component_list)))
        
        return layers 



