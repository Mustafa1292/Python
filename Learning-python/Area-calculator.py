# -*- coding: utf-8 -*-
import math

# Some useful constants here
PAINT_COVERAGE = 400 # square feet per gallon
TILE_COVERAGE = 16 # tiles per square foot

# The main part of the program begins here
length = int(input("Enter the room length in feet: "))
width = int(input("Enter the room width in feet: "))
height = int(input("Enter the room height in feet: "))

# Perform the computations here
paint_area = 2*(length * height + width * height) + length * width
paint_volume = math.ceil(paint_area / PAINT_COVERAGE) # compute and round up paint volume
floor_tiles = math.ceil(length * width * TILE_COVERAGE)

# Output the results
print()
print("The total paint needed to cover the walls and ceiling is", paint_volume, "gallons.")
print("The total number of tiles to cover the floor is", floor_tiles, ".")
 
