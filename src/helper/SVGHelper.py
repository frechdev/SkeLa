from enum import Enum
from typing import List
import numpy as np

class FontSize(Enum):
    SMALL = 0.3
    NORMAL = 0.5
    HUGE = 0.7

class StrokeWidth(Enum):
    THIN = 0.01
    NORMAL = 0.03
    THICK = 0.05

def gen_style_string(class_name, *argv) -> str:
    string = ''
    string += f'.{class_name} {{\n'
    
    for arg in argv:
        string += f'{arg};\n'

    string += '}'
    return string

def gen_line_string(pt1:np.ndarray, pt2:np.ndarray, class_name:str = None, adds:str = None) -> str:
    string = '<line '
    if class_name:
        string += f'class="{class_name}" '
    if adds:
        string += f'{adds} '
    string += f'x1="{pt1[0]}" '
    string += f'y1="{pt1[1]}" '
    string += f'x2="{pt2[0]}" '
    string += f'y2="{pt2[1]}" '
    string += f'/>'

    return string

def gen_path_string(pts:List[np.array], is_closed_path:bool, class_name:str = None, adds:str = None) -> str:
    string = '<path '
    if class_name:
        string += f'class="{class_name}" '
    if adds:
        string += f'{adds} '
    
    sub_string = ''
    for i in range(0,len(pts)):
        if i == 0:
            sub_string += 'M'
        else:
            sub_string += ' L'
        
        pt = pts[i]
        sub_string += f'{pt[0]} {pt[1]}'

    if is_closed_path:
        sub_string += ' Z'

    string += f'd="{sub_string}" '
    string += f'/>'

    return string

def gen_circle_string(center:np.ndarray,radius:int, class_name:str = None, adds:str = None) -> str:
    string = '<circle '
    
    if class_name:
        string += f'class="{class_name}" '
    if adds:
        string += f'{adds} '

    string += f'cx="{center[0]}" '
    string += f'cy="{center[1]}" '
    string += f'r="{radius}" '
    string += f'/>'

    return string

def gen_text_string(anchor:np.ndarray, font_size:FontSize, content:str, class_name:str = None, adds:str = None) -> str:
    
    string = f'<text '

    string += f'font-size="{font_size.value}" '

    if class_name:
        string += f'class="{class_name}" '

    if adds:
        string += f'{adds} '

    string += f'x="{anchor[0]}" y="{anchor[1]}">{content}</text>'
    
    return string

