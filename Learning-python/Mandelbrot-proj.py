# -*- coding: utf-8 -*-


def is_in_Mandelbrot(c):
    z = 0 # Start the iterations with zero
    for iteration in range(10000): # Loop for a large number of iterations
        z = z*z + c # Update the value of z
        if abs(z) > 2: # If z ever gets too large
            return False # It is outside the set
    # If all the iterations are complete
    return True # The point is inside the set

width = int(input("Please enter the width: "))
height = int(input("Please enter the height: "))

for row in range(height):
    y = 1 - 2.0 * row / (height - 1)
    for col in range(width):
        x = -2 + 3.0 * col / (width - 1)
        z = complex(x,y)
        
        if is_in_Mandelbrot(z):
            print("@", end="")
        else:
            print(" ", end="")
    #the for loop on col is finished
    print()
#the for loop on row is finished here
