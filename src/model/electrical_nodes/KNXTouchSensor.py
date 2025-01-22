from model.electrical_nodes.ElectricalNode import ElectricalNode


class KNXTouchSensor(ElectricalNode):
    '''
    Symbol-Source: https://gallery.proficad.com/schaltzeichen
    '''
    _original_width = 111
    _original_height = 81
    _scale = 0.2

    
        
    def get_svg_definition_string(self):
        stroke_width = 0.3
        
        definition_string_list = [] 

        super_svg_definition_string = super().get_svg_definition_string()
        if super_svg_definition_string is not None:
            definition_string_list.append(super_svg_definition_string)

        x_scale = self._scale
        y_scale = self._scale

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Symbol">')
        definition_string_list.append(f'<rect x="{10*x_scale}" y="{0.1*y_scale}" width="{100*x_scale}" height="{80*y_scale}" fill="white" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{0*x_scale}" y1="{40*y_scale}" x2="{10*x_scale}" y2="{40*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{30*x_scale}" y1="{0*y_scale}" x2="{30*x_scale}" y2="{80*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{18*x_scale}" y1="{15*y_scale}" x2="{18*x_scale}" y2="{65*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{22*x_scale}" y1="{15*y_scale}" x2="{22*x_scale}" y2="{65*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<polygon points="{15*x_scale},{15*y_scale} {25*x_scale},{15*y_scale} {20*x_scale},{7*y_scale}"  fill="none" stroke="black" stroke-width="{stroke_width}px"/>')
        definition_string_list.append(f'<polygon points="{15*x_scale},{65*y_scale} {25*x_scale},{65*y_scale} {20*x_scale},{73*y_scale}"   fill="none" stroke="black" stroke-width="{stroke_width}px"/>')
        definition_string_list.append(f'<line x1="{30*x_scale}" y1="{80*y_scale}" x2="{110*x_scale}" y2="{0*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<circle cx="{95*x_scale}" cy="{65*y_scale}" r="{10*x_scale}" fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<circle cx="{95*x_scale}" cy="{65*y_scale}" r="{5*x_scale}"  fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)

    def get_size(self):
        width = self._original_width*self._scale
        height = self._original_height*self._scale
        
        size = (width, height)
        return size
    