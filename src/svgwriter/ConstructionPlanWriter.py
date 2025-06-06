from io import BytesIO
import math
import numpy as np
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3
from svglib.svglib import svg2rlg
from typing import Dict, List, cast
from exceptions.InputError import InputError
import helper.VersionHelper as VersionHelper
import helper.SVGHelper as SVGHelper
import helper.PlanCalculations as PlanCalculations
from model.AreaDimension import AreaDimension
from model.Label import Label
from model.PlanComponent import PlanComponent
from model.Room import Room
from model.Settings import Settings
from svgwriter import ZHierarchy
from model.Shape import Shape
from model.Component import Component
from model.ConstructionPlanSet import ConstructionPlanSet
from model.MetaInformation import MetaInformation
from svgwriter.PlanType import PlanType, get_clear_name


class ConstructionPlanWriter:
    plan_margin = 1
    
    def __init__(self, file_path_base, constructionPlanSet:ConstructionPlanSet, debug_mode):
        self.file_path_base = file_path_base
        self.constructionPlanSet = constructionPlanSet
        self.debug_mode = debug_mode
        self.scale_divisor = constructionPlanSet.settings.scale_divisor

        match constructionPlanSet.settings.page_size:
            case 'A4':
                self.pagesize = A4
                self.page_width, self.page_height = 21, 29.7
            case 'A3':
                self.pagesize = A3
                self.page_width, self.page_height = 29.7, 42
            case _:
                raise ValueError(f'Page size {constructionPlanSet.settings['page_size']} is not supported')
                
    def write(self, is_savig_svg:bool):
        component_list:List[Component] = []
        
        if next((obj for obj in self.constructionPlanSet.component_list if isinstance(obj, MetaInformation) and obj.title == "Seite"), None):
            raise InputError('Meta-Information with title "Seite" is used internally and forbidden for input.')
        component_list.append(MetaInformation(title = 'Seite'))

        if next((obj for obj in self.constructionPlanSet.component_list if isinstance(obj, MetaInformation) and obj.title == "Plan"), None):
            raise InputError('Meta-Information with title "Plan" is used internally and forbidden for input.')
        component_list.append(MetaInformation(title = 'Plan'))

        if next((obj for obj in self.constructionPlanSet.component_list if isinstance(obj, MetaInformation) and obj.title == "Massstab"), None):
            raise InputError('Meta-Information with title "Massstab" is used internally and forbidden for input.')
        component_list.append(MetaInformation(title = 'Massstab', content = f'1 : {self.scale_divisor}'))
        
        if next((obj for obj in self.constructionPlanSet.component_list if isinstance(obj, MetaInformation) and obj.title == "Ebene"), None):
            raise InputError('Meta-Information with title "Ebene" is used internally and forbidden for input.')
        component_list.append(MetaInformation(title = 'Ebene'))

        plan_components:list[PlanComponent] = list(filter(lambda n: (isinstance(n, PlanComponent)), self.constructionPlanSet.component_list))
        for plan_component in plan_components:
            debug_components = plan_component.create_debug_components()
            if debug_components:
                component_list.extend(debug_components)
        
        component_list.extend(self.constructionPlanSet.component_list)

        room_components:list[Room] = list(filter(lambda n: (isinstance(n, Room)), self.constructionPlanSet.component_list))
        for room_component in room_components:
            component_list.append(AreaDimension(room_component))
        
        layers = sorted(self.constructionPlanSet.get_layers())
        pdf_buffer = BytesIO()
        pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=self.pagesize)
        page_counter = 1
        for layer in layers:
            for plan_type in PlanType:
                layer_meta_information = next((obj for obj in component_list if isinstance(obj, MetaInformation) and obj.title == "Ebene"), None)
                layer_meta_information.content = f'{layer}'
                
                plan_type_meta_information = next((obj for obj in component_list if isinstance(obj, MetaInformation) and obj.title == "Plan"), None)
                plan_type_meta_information.content = f'{get_clear_name(plan_type)}'
                
                page_counter_meta_information = next((obj for obj in component_list if isinstance(obj, MetaInformation) and obj.title == "Seite"), None)
                page_counter_meta_information.content = f'{page_counter}'
                
                component_list_for_current_plan = list(filter(
                    lambda n: (
                        (n.layer == layer or n.layer is None) and 
                        plan_type in n.plan_belonging and 
                        (self.debug_mode or not n.is_debug)
                        ), component_list))
                
                svg_content = self.make_svg_content(component_list_for_current_plan, self.constructionPlanSet.settings)
                
                svg_buffer = BytesIO(svg_content.encode('utf-8'))
                
                drawing = svg2rlg(svg_buffer)
                renderPDF.draw(drawing, pdf_canvas, 0, 0)
                pdf_canvas.showPage()

                if is_savig_svg:
                    self.save_svg(layer, plan_type, svg_buffer)            
                    
                page_counter += 1

        pdf_canvas.save()
        
        pdf_file_path = f'{self.file_path_base}.pdf'
        pdf_buffer.seek(0)
        with open(pdf_file_path, 'wb') as f:
            f.write(pdf_buffer.read())

    def make_svg_content(self, component_list:List[Component], settings:Settings):
        svg_content_list = []
        svg_content_list.append(self.make_header(self.page_width, self.page_height, component_list))
        
        meta_information_list:List[MetaInformation] = list(filter(lambda n: isinstance(n, MetaInformation), component_list))
        plan_border_content, meta_inforamtion_height = self.make_plan_border(self.page_width, self.page_height, self.plan_margin, settings.compass_rotation, meta_information_list)
        svg_content_list.append(plan_border_content)

        body_heigth = self.page_height - meta_inforamtion_height
        svg_content_list.append(self.make_body(self.page_width, body_heigth, component_list))

        svg_content_list.append(self.make_footer())
        return '\n'.join(svg_content_list)

    def make_header(self, page_width, page_height, component_list:List[Component]):
        header_content_list = []
        header_content_list.append(f'<svg width="{page_width}cm" height="{page_height}cm" xmlns="http://www.x3.org/2000/svg" viewBox="0 0 {page_width} {page_height}">')
        
        style_content_list = []
        style_content_list.append(SVGHelper.gen_style_string('plan-boarder', 'fill: none', 'stroke: black', f'stroke-width: {SVGHelper.StrokeWidth.THICK.value}'))
        style_content_list.append(SVGHelper.gen_style_string('watermark-text', 'font-family: monospace'))

        definition_content_list = []

        seen_classes = set()
        for component in component_list:
            component_class = type(component)
            if component_class not in seen_classes:
                svg_style_string = component.get_svg_style_string()
                if svg_style_string is not None:
                    style_content_list.append(svg_style_string)
                
                svg_definition_string = component.get_svg_definition_string()
                if svg_definition_string is not None:
                    definition_content_list.append(svg_definition_string)

                seen_classes.add(component_class)
        
        header_content_list.append('<style>')
        header_content_list.extend(style_content_list)
        header_content_list.append('</style>')

        header_content_list.append('<defs>')
        header_content_list.extend(definition_content_list)
        header_content_list.append('</defs>')

        return '\n'.join(header_content_list)

    def make_plan_border(self, page_width, page_height, margin, compass_rotation, meta_information_list:List[MetaInformation]):
        plan_border_width = page_width-margin*2
        plan_border_heigth = page_height-margin*2
    	
        plan_border_content_list = []

     
        plan_border_content_list.append(f'<rect class="plan-boarder" width="{plan_border_width}" height="{plan_border_heigth}" x="{margin}" y="{margin}"/>')
        
        maj, min, patch, rev = VersionHelper.get_version()
        version_str=VersionHelper.version_to_str(maj, min, patch, rev)

        watermark_text_1 = f'Created with SkeLa v{version_str}'
        watermark_text_2 = '(https://github.com/frechdev/SkeLa)'
        
        plan_border_content_list.append(f'<text class="watermark-text" font-size="0.3" x="{margin}" y="{margin + plan_border_heigth + 0.3}">{watermark_text_1}<tspan x="{margin}" dy="0.3">{watermark_text_2}</tspan></text>')

        info_box_width = plan_border_width/3
        info_box_height = 1.5
        info_box_margin = 0.1
        info_box_key_y_offset = 0.4
        info_box_text_y_offset = -0.2

        counter:int = -1
        for meta_information in meta_information_list:
            counter += 1

            info_box_x = plan_border_width + margin - info_box_width * (counter%2 + 1)
            info_box_y = plan_border_heigth + margin - info_box_height * (int(counter/2) + 1)

            plan_border_content_list.append(f'<rect class="plan-boarder" width="{info_box_width}" height="{info_box_height}" x="{info_box_x}" y="{info_box_y}" />')
            plan_border_content_list.append(f'<text class="{type(meta_information).__name__}-Title" font-size="0.5" x="{info_box_x+info_box_margin}" y="{info_box_y+info_box_margin+info_box_key_y_offset}">{meta_information.title}</text>')
            plan_border_content_list.append(f'<text class="{type(meta_information).__name__}-Content" font-size="0.5" x="{info_box_x + info_box_width/2}" y="{info_box_y + info_box_height - info_box_margin + info_box_text_y_offset}">{meta_information.content}</text>')

        plan_border_content_list.append(f'<g transform="translate({margin+info_box_width/2} {page_height-margin-3})">')
        plan_border_content_list.append(f'<g transform="rotate({compass_rotation} 0 0)">')
        plan_border_content_list.append(f'<circle r="2" stroke="black" stroke-width="0.1" fill="none" />')
        plan_border_content_list.append(f'<circle r="1" stroke="black" stroke-width="0.1" fill="none" />')
        plan_border_content_list.append(f'<circle r="0.1" stroke="black" stroke-width="0.1" fill="black" />')
        plan_border_content_list.append(f'<line y1="-1" y2="1" stroke="black" stroke-width="0.1" />')
        plan_border_content_list.append(f'<text x="0" y="-1.2" font-family="monospace" font-size="1" text-anchor="middle" fill="black">N</text>')
        plan_border_content_list.append(f'<text x="0" y="1.8" font-family="monospace" font-size="1" text-anchor="middle" fill="black">S</text>')
        plan_border_content_list.append(f'<text x="-1.5" y="0.3" font-family="monospace" font-size="1" text-anchor="middle" fill="black">W</text>')
        plan_border_content_list.append(f'<text x="1.5" y="0.3" font-family="monospace" font-size="1" text-anchor="middle" fill="black">E</text>')
        plan_border_content_list.append('</g></g>')
        
        return '\n'.join(plan_border_content_list), info_box_height * (int(counter/2) + 1)

    def make_body(self, body_width, body_heigth, component_list:List[Component]):
        plan_component_list:List[PlanComponent] = list(filter(
            lambda n: isinstance(n, PlanComponent) and not n.is_hidden,
            component_list
            ))
        
        if (not self.debug_mode):
            plan_component_list = list(filter(lambda n: not n.is_debug, plan_component_list))

        x_min = math.inf
        x_max = -math.inf
        y_min = math.inf
        y_max = -math.inf

        shape_component_list:List[Shape] = list(filter(lambda n: isinstance(n, Shape), plan_component_list))
        boundry_list = list(map(lambda n: n.get_global_boundry(), shape_component_list))
        min_coords_array = np.array(list(map(lambda n: n[0], boundry_list)))
        max_coords_array = np.array(list(map(lambda n: n[1], boundry_list)))
        min_coords = min_coords_array.min(axis=0)
        max_coords = max_coords_array.max(axis=0)
        
        transformed_min_coords = PlanComponent.transform_point_for_plan(min_coords, self.scale_divisor)
        transformed_max_coords = PlanComponent.transform_point_for_plan(max_coords, self.scale_divisor)
        
        x_offset = body_width/2 - (transformed_max_coords[0] - transformed_min_coords[0])/2
        y_offset = body_heigth/2 - (transformed_max_coords[1] - transformed_min_coords[1])/2 - transformed_min_coords[1]

        body_content_list = []
        body_content_list.append(f'<g transform="translate({x_offset} {y_offset})">')

        plan_component_list = ZHierarchy.sort_by_z_hierarchy(plan_component_list)
        
        for plan_component in plan_component_list:
            
            body_content_list.append(plan_component.get_svg_string(self.scale_divisor))
                      
            if isinstance(plan_component, Shape):
                min_coords, max_coords = plan_component.get_global_boundry()
                
                x_min_shape = transformed_min_coords[0]
                x_max_shape = transformed_max_coords[0]
                y_min_shape = transformed_min_coords[1]
                y_max_shape = transformed_max_coords[1]

                if (x_min_shape < x_min): x_min = x_min_shape
                if (x_max_shape > x_max): x_max = x_max_shape
                if (y_min_shape < y_min): y_min = y_min_shape
                if (y_max_shape > y_max): y_max = y_max_shape

        body_content_list.append('</g>')

        return '\n'.join(body_content_list)

    def make_footer(self):
        return '</svg>'

    def plan_type_to_clear_name(self, plan_type:PlanType):
        klartext = []
        for flag in PlanType:
            if flag in self:
                klartext.append(self._klarname_mapping[flag])

    def save_svg(self, layer, plan_type:PlanType, svg_buffer):
        svg_file_path = f'{self.file_path_base}_{layer}_{plan_type}.svg'
        svg_buffer.seek(0)
            
        with open(svg_file_path, 'wb') as svg_file:
            svg_file.write(svg_buffer.read())
