from model.electrical_nodes.ElectricalNode import ElectricalNode


class SocketData(ElectricalNode):
    '''
    Symbol-Source: https://gallery.proficad.com/schaltzeichen
    '''
    _original_width = 20
    _original_height = 20
    _scale = 0.5

    def get_svg_definition_string(self):
        stroke_width = 0.3
        
        definition_string_list = [] 

        super_svg_definition_string = super().get_svg_definition_string()
        if super_svg_definition_string is not None:
            definition_string_list.append(super_svg_definition_string)

        x_scale = self._scale
        y_scale = self._scale

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Symbol">')
        definition_string_list.append(f'<line x1="{0*x_scale}" y1="{10*y_scale}" x2="{10*x_scale}" y2="{10*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{10*x_scale}" y1="{0*y_scale}" x2="{10*x_scale}" y2="{20*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{10*x_scale}" y1="{0.1*y_scale}" x2="{20*x_scale}" y2="{0.1*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{10*x_scale}" y1="{20*y_scale}" x2="{20*x_scale}" y2="{20*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{10*x_scale}" y1="{0.1*y_scale}" x2="{20*x_scale}" y2="{20*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{10*x_scale}" y1="{20*y_scale}" x2="{20*x_scale}" y2="{0.1*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)

    def get_size(self):
        width = self._original_width*self._scale
        height = self._original_height*self._scale
        
        size = (width, height)
        return size
        