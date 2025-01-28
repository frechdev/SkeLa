from model.electrical_nodes.ElectricalNode import ElectricalNode


class SocketPower(ElectricalNode):
    '''
    Symbol-Source: https://gallery.proficad.com/schaltzeichen
    '''
    _original_width = 20
    _original_height = 20
    multiplicity:int = 1

    
        
    def get_svg_definition_string(self):
        stroke_width = 1
        
        definition_string_list = [] 

        super_svg_definition_string = super().get_svg_definition_string()
        if super_svg_definition_string is not None:
            definition_string_list.append(super_svg_definition_string)

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Node-Single">')
        definition_string_list.append(f'<line x1="10" y1="0" x2="10" y2="20" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="0" y1="10" x2="10" y2="10" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<path d="M20 0 A10 10 0 0 0 20 20" fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'</symbol>')

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Node-Double">')
        definition_string_list.append(f'<line x1="10" y1="0" x2="10" y2="20" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="0" y1="10" x2="10" y2="10" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<path d="M20 0 A10 10 0 0 0 20 20" fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="12" y1="20" x2="16" y2="16" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<text x="12" y="20" font-size="6pt" font-family="monospace" font-weight="bold" transform="rotate(90 12 20)">2</text>')
        definition_string_list.append(f'</symbol>')

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Node-Triple">')
        definition_string_list.append(f'<line x1="10" y1="0" x2="10" y2="20" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="0" y1="10" x2="10" y2="10" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<path d="M20 0 A10 10 0 0 0 20 20" fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="0" y1="10" x2="10" y2="10" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="12" y1="20" x2="16" y2="16" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<text x="12" y="20" font-size="6pt" font-family="monospace" font-weight="bold" transform="rotate(90 12 20)">3</text>')
        definition_string_list.append(f'</symbol>')

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Node-Quadruple">')
        definition_string_list.append(f'<line x1="10" y1="0" x2="10" y2="20" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="0" y1="10" x2="10" y2="10" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<path d="M20 0 A10 10 0 0 0 20 20" fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="0" y1="10" x2="10" y2="10" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="12" y1="20" x2="16" y2="16" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<text x="12" y="20" font-size="6pt" font-family="monospace" font-weight="bold" transform="rotate(90 12 20)">4</text>')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)

    def get_svg_string(self, scale_divisor):
        svg_string = super().get_svg_string(scale_divisor)
        
        match self.multiplicity:
            case 1:
                svg_string = svg_string.replace(f'"#{type(self).__name__}-Node"', f'"#{type(self).__name__}-Node-Single"')
            case 2:
                svg_string = svg_string.replace(f'"#{type(self).__name__}-Node"', f'"#{type(self).__name__}-Node-Double"')
            case 3:
                svg_string = svg_string.replace(f'"#{type(self).__name__}-Node"', f'"#{type(self).__name__}-Node-Triple"')
            case 4:
                svg_string = svg_string.replace(f'"#{type(self).__name__}-Node"', f'"#{type(self).__name__}-Node-Quadruple"')
            case _:
                raise NotImplementedError()
        
        return svg_string
        