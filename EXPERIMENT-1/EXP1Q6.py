import math
def area_of_triangle(base, height):
    return 0.5 * base * height
def area_of_rectangle(length, width):
    return length * width
def area_of_circle(radius):
    return math.pi * radius ** 2
def area_of_sphere(radius):
    return 4 * math.pi * radius ** 2
print("Area of triangle:", area_of_triangle(10, 5))
print("Area of rectangle:", area_of_rectangle(10, 5))
print("Area of circle:", area_of_circle(5))
print("Area of sphere:", area_of_sphere(5))