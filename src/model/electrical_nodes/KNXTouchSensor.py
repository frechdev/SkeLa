from model.electrical_nodes.ElectricalNode import ElectricalNode


class KNXTouchSensor(ElectricalNode):
    '''
    Symbol-Source: https://gallery.proficad.com/schaltzeichen
    '''
    _original_width = 20
    _original_height = 20

    def get_svg_definition_string(self):
        stroke_width = 1
        
        definition_string_list = [] 

        super_svg_definition_string = super().get_svg_definition_string()
        if super_svg_definition_string is not None:
            definition_string_list.append(super_svg_definition_string)

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Node">')
        definition_string_list.append(f'<rect x="0" y="0.1" width="20" height="20" fill="white" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<line x1="0" y1="20" x2="20" y2="0" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<circle cx="{14}" cy="{14}" r="{3.5}" fill="none" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<circle cx="{14}" cy="{14}" r="{1.5}"  fill="none" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)

