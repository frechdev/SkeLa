from model.electrical_nodes.ElectricalNode import ElectricalNode


class KNXBusInterface (ElectricalNode):
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
        definition_string_list.append(f'<rect x="10" y="0.1" width="10" height="20" fill="white" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<line x1="0" y1="10" x2="10" y2="10" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<line x1="14" y1="5" x2="14" y2="15" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<line x1="16" y1="5" x2="16" y2="15" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<polygon points="12,5 15,2 18,5"  fill="black"/>')
        definition_string_list.append(f'<polygon points="12,15 15,18 18,15"  fill="black"/>')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)

    def get_size(self):
        width = self._original_width
        height = self._original_height
        
        size = (width, height)
        return size
    