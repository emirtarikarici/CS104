import math

# Declare PI only once in the file.
PI = 3.141592


def get_area_of_ellipse(a, b):
    return PI * a * b


def get_lateral_area(a, b, h):
    return 2 * PI * math.sqrt((a ** 2 + b ** 2) / 2) * h


def get_total_surface_area(a, b, h):
    return 2 * get_area_of_ellipse(a, b) + get_lateral_area(a, b, h)


semi_major_axis = 7.5
semi_minor_axis = 6.
height = 12.2

# Expected value is ~800.
print(get_total_surface_area(semi_minor_axis, semi_major_axis, height))
