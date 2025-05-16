import helper.SVGHelper as SVGHelper
from exceptions.MissingAttributeError import MissingAttributeError
from model.Component import Component


class MetaInformation(Component):
    title: str
    content: str = ''

    def get_svg_style_string(self):
        style_string_list = []
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Title', 'font-family: monospace', 'text-anchor: start'))
        style_string_list.append(SVGHelper.gen_style_string(f'{type(self).__name__}-Content', 'font-family: monospace', 'font-weight: bold', 'text-anchor: middle'))
        return '\n'.join(style_string_list) 
    
    def validate(self):
        if not self.title:
            raise MissingAttributeError('title', __name__)

                
        return super().validate()
        
    