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

def rotation_matrix(angle_degrees: float) -> np.ndarray:
    """
    Creates a 2D-rotation matrix for an angle in degrees.

    Parameters:
    - angle_degrees (float): The rotation angle in degrees.

    Returns:
    - np.ndarray: The rotation matrix.
    """

    while angle_degrees < 0:
        angle_degrees += 360

    angle_radians = np.radians(angle_degrees)
    cos_theta = np.cos(angle_radians)
    sin_theta = np.sin(angle_radians)
    return np.array([
        [cos_theta, -sin_theta],
        [sin_theta, cos_theta]
    ])

def calc_polygon_area(points:np.ndarray):
    n = len(points)
    area = 0
    
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # Der nächste Punkt, mit Wrap-around zum ersten Punkt
        area += x1 * y2 - x2 * y1
    
    return abs(area) / 2

