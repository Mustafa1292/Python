# -*- coding: utf-8 -*-
"""
A sample of one possible solution for the assignment
Area calculation and sealant coverage for a floor
"""

SEALANT_COVERAGE = 6 # The number of square meters that one L of sealant covers
BOTTLE_SIZE = 2 # The size of a bottle of sealant in L

# Use this function to round up a number
def RoundUp(number):
    return int(number + 0.99999)

# Get the input from the user
length = int(input("Enter the length of the room (m):"))
width = int(input("Enter the width of the room (m):"))
cost = int(input("Enter the cost per bottle ($):"))

# Compute the results 
area = length * width
num_liters = RoundUp(area / SEALANT_COVERAGE) 
num_bottles = RoundUp(num_liters / BOTTLE_SIZE)

# Print out the results in a nice format
print("="*40)
print("Room area     (m2) =", area)
print("Sealant needed (L) =", num_liters)
print("Bottles needed     =", num_bottles)
print("Total Cost     ($) =", 2*num_bottles)
print("="*40)
