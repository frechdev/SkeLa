from typing import List
import numpy as np

def ref_point_list(point_list:List[np.ndarray], reference:np.ndarray) -> List[np.ndarray]:
    return list(map(lambda n: ref_point(n,reference), point_list))

def ref_point(point:np.ndarray, reference:np.ndarray) -> np.ndarray:
    return np.add(point,reference)

def scale_point_list_for_plan(point_list:List[np.ndarray], scale_divisor:int) -> List[np.ndarray]:
    return list(map(lambda n: scale_point_for_plan(n, scale_divisor), point_list))

def scale_point_for_plan(point:np.ndarray, scale_divisor:int) -> np.ndarray:
    return cm_to_dots(point)/scale_divisor

def invert_y_list(point_list:List[np.ndarray]) -> List[np.ndarray]:
    return list(map(lambda n: invert_y(n), point_list))

def invert_y(point:np.ndarray):
    return np.matmul(point, np.array([[1, 0], [0, -1]]))

def cm_to_dots(value):
    dpi = 72
    cm_per_inch = 2.54

    return value*dpi/cm_per_inch
