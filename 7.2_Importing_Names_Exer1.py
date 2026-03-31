"""
Party favors
The following program does not run correctly because of name collisions. 
Fix the program by modifying import statements, function calls, and variable assignments.
"""

import area
import math

def cone(radius, height):
    """Gets the volume of a cone."""
    return math.pi * radius**2 * height/3

def sphere(radius):
    """Gets the volume of a sphere."""
    return 4/3 * math.pi * radius**3

# A bouncy ball is 2 inches in diameter.
ball_area = area.sphere(1)
ball_volume = sphere(1)
print("Bouncy ball area:", round(ball_area))
print("Bouncy ball volume:", round(ball_volume))

# A cone hat is 10 inches in diameter and 8 inches tall.
cone_area = area.cone(5, 8)
cone_volume = cone(5, 8)
print("Cone hat area:", round(cone_area))
print("Cone hat volume:", round(cone_volume))