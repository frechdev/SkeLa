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
        definition_string_list.append(f'<rect x="10cm" y="0.1cm" width="10cm" height="20cm" fill="white" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="0cm" y1="10cm" x2="10cm" y2="10cm" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="14cm" y1="5cm" x2="14cm" y2="15cm" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="16cm" y1="5cm" x2="16cm" y2="15cm" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<polygon points="12cm,5cm 15cm,2cm 18cm,5cm"  fill="black"/>')
        definition_string_list.append(f'<polygon points="12cm,15cm 15cm,18cm 18cm,15cm"  fill="black"/>')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)

    def get_size(self):
        width = self._original_width
        height = self._original_height
        
        size = (width, height)
        return size
    