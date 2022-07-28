# -*- coding: utf-8 -*-
"""
Sample of one possible solution for the assignment
Area between a circle and a hexagon
"""

import math

PI = math.pi # Use a nice constant here for easy calculations

# Input the radius from the user and convert it to a float value
radius = float(input("Please enter the radius of the circle:"))

# Calculate the areas
circle_area = PI * radius**2
hex_area = (3 * math.sqrt(3) / 2) * radius**2
shaded_area = circle_area - hex_area

# Print the results with a nice format
print("="*40)
print("Circle area  =", circle_area)
print("Hexagon area =", hex_area)
print("Shaded area  =", shaded_area)
print("="*40)

### Bonus ###
# r = 1.839871
