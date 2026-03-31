"""
Printing right triangle area
Write a function, print_area(), that takes in the base and height of a right triangle and prints the triangle's area. 
The area of a right triangle is bh/2, where b is the base and h is the height.
"""

# Define print_area()
def print_area(base, height):
    area = (base * height) / 2
    print('Triangle area:', area)

base = float(input())
height = float(input())
print_area(base, height)