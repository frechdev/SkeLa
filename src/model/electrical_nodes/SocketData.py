from model.electrical_nodes.ElectricalNode import ElectricalNode


class SocketData(ElectricalNode):
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
        definition_string_list.append(f'<line x1="0" y1="10" x2="10" y2="10" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<path d="M10 20 L20 0 10 0 10 20 20 20 10 0" fill="none" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)
        