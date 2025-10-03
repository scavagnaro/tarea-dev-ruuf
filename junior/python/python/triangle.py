import math
import functools

total_time = 0

@functools.cache
def calculate_panels(panel_width: int, panel_height: int, triangule_base: int, triangule_height: int) -> int:
    # Implementa acá tu solución
        
    if triangule_base <= 0 or triangule_height <= 0:
        return 0
    
    if panel_width <= 0 or panel_height <= 0:
        return float("inf")
    
    if triangule_height < panel_height or triangule_base < panel_width:
        return 0
    
    base_angle = calculate_base_angles(triangule_base, triangule_height)
        
    #Base of the sub-triangule when using normal panel
    sub_triangule_base_normal = (triangule_height - panel_height) / math.tan(math.radians(base_angle)) * 2
            
    normal_panels = calculate_panels(panel_width, panel_height, 
                           sub_triangule_base_normal, 
                           triangule_height - panel_height) + (sub_triangule_base_normal // panel_width)


    #Base of the sub-triangule when using rotated panel
    sub_triangule_base_rotated = (triangule_height - panel_width) / math.tan(math.radians(base_angle)) * 2

    rotated_panels = calculate_panels(panel_width, panel_height, 
                           sub_triangule_base_rotated, 
                           triangule_height - panel_width) + (sub_triangule_base_rotated // panel_height)

    return max(normal_panels, rotated_panels)

functools.cache
def calculate_base_angles(triangule_base: int, triangule_height: int) -> float:
    angle_radians = math.atan(triangule_height / (triangule_base / 2))
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees


if __name__ == "__main__":
    print(calculate_panels(1, 2, 8, 6))  # Debería retornar 8
    print(calculate_panels(2, 2, 16, 12))  # Debería retornar 18
