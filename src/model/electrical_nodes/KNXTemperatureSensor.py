from model.electrical_nodes.ElectricalNode import ElectricalNode


class KNXTemperatureSensor(ElectricalNode):
    '''
    Symbol-Source: https://gallery.proficad.com/schaltzeichen
    '''
    _original_width = 20
    _original_height = 20
    has_controller: bool = False

    def get_svg_definition_string(self):
        stroke_width = 1
        
        definition_string_list = [] 

        super_svg_definition_string = super().get_svg_definition_string()
        if super_svg_definition_string is not None:
            definition_string_list.append(super_svg_definition_string)

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Node">')
        definition_string_list.append(f'<rect x="0" y="0.1" width="20" height="20" fill="white" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<line x1="0" y1="20" x2="20" y2="0" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<text x="15" y="18" font-size="3mm" font-family="monospace" font-weight="bold" text-anchor="middle">T</text>')
        definition_string_list.append(f'</symbol>')

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Node-Controller">')
        definition_string_list.append(f'<rect x="0" y="0.1" width="20" height="20" fill="white" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<line x1="0" y1="20" x2="20" y2="0" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<path d="M2 7 L7 7 L7 3 L12 3" fill="none" stroke="black" stroke-width="{stroke_width}" />')
        definition_string_list.append(f'<text x="15" y="18" font-size="3mm" font-family="monospace" font-weight="bold" text-anchor="middle">T</text>')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)

    def get_svg_string(self, scale_divisor):
        svg_string = super().get_svg_string(scale_divisor)
        
        if self.has_controller:
            svg_string = svg_string.replace(f'"#{type(self).__name__}-Node"', f'"#{type(self).__name__}-Node-Controller"')
        
        return svg_string
