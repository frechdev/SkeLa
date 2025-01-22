from model.electrical_nodes.ElectricalNode import ElectricalNode


class SocketPower(ElectricalNode):
    '''
    Symbol-Source: https://gallery.proficad.com/schaltzeichen
    '''
    _original_width = 20
    _original_height = 20
    _scale = 0.5
    multiplicity:int = 1

    
        
    def get_svg_definition_string(self):
        stroke_width = 0.3
        
        definition_string_list = [] 

        super_svg_definition_string = super().get_svg_definition_string()
        if super_svg_definition_string is not None:
            definition_string_list.append(super_svg_definition_string)

        x_scale = self._scale
        y_scale = self._scale

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Symbol-Single">')
        definition_string_list.append(f'<line x1="{10*x_scale}" y1="{0*y_scale}" x2="{10*x_scale}" y2="{20*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{0*x_scale}" y1="{10*y_scale}" x2="{10*x_scale}" y2="{10*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<path d="M{20*x_scale} {0*y_scale} A{10*x_scale} {10*y_scale} 0 0 0 {20*x_scale} {20*y_scale}" fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'</symbol>')

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Symbol-Double">')
        definition_string_list.append(f'<line x1="{10*x_scale}" y1="{0*y_scale}" x2="{10*x_scale}" y2="{20*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{0*x_scale}" y1="{10*y_scale}" x2="{10*x_scale}" y2="{10*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<path d="M{20*x_scale} {0*y_scale} A{10*x_scale} {10*y_scale} 0 0 0 {20*x_scale} {20*y_scale}" fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{12*x_scale}" y1="{20*y_scale}" x2="{16*x_scale}" y2="{16*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<text x="{12*x_scale}" y="{20*x_scale}" font-size="{6*y_scale}pt" font-family="monospace" font-weight="bold" transform="rotate(90 {12*x_scale} {20*x_scale})">2</text>')
        definition_string_list.append(f'</symbol>')

        definition_string_list.append(f'<symbol id="{type(self).__name__}-Symbol-Triple">')
        definition_string_list.append(f'<line x1="{10*x_scale}" y1="{0*y_scale}" x2="{10*x_scale}" y2="{20*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{0*x_scale}" y1="{10*y_scale}" x2="{10*x_scale}" y2="{10*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<path d="M{20*x_scale} {0*y_scale} A{10*x_scale} {10*y_scale} 0 0 0 {20*x_scale} {20*y_scale}" fill="none" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{0*x_scale}" y1="{10*y_scale}" x2="{10*x_scale}" y2="{10*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<line x1="{12*x_scale}" y1="{20*y_scale}" x2="{16*x_scale}" y2="{16*y_scale}" stroke="black" stroke-width="{stroke_width}px" />')
        definition_string_list.append(f'<text x="{12*x_scale}" y="{20*x_scale}" font-size="{6*y_scale}pt" font-family="monospace" font-weight="bold" transform="rotate(90 {12*x_scale} {20*x_scale})">3</text>')
        definition_string_list.append(f'</symbol>')

        return '\n'.join(definition_string_list)

    def get_size(self):
        width = self._original_width*self._scale
        height = self._original_height*self._scale
        
        size = (width, height)
        return size
    