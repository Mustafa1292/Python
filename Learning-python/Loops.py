# -*- coding: utf-8 -*-
"""
We use Newton's method to compute a square root.
"""

import math # We'll need this for sqrt to compute the "correct" answer

def get_number():
    number = float(input("Please enter a number: "))
    while number < 0:
        print("The number you entered was negative.")
        print("Please enter a positive number.")
        number = float(input("Please enter a number: "))
        
    return number

def newton(num, steps):
    guess = 2 # Why 2? It's an ok place to start
    count = 0
    while count < steps:
        guess = (guess + num/guess)/2
        count += 1

    return guess

def work(value):
    print("Steps = Value")
    i = 1
    while i <= 16:
        print(i,"=", newton(value,i))
        i *= 2

    print("sqrt =", math.sqrt(value))
    print("="*40)

#This part of the code needs a little more work to match the output
# We need to change up the order somewhat, but how???
value = get_number() # Ask first
while value != 0: #  Then check to see if we have to do any more work
    work(value) # Do some work
    value = get_number() # Get the next value

print("Thank you, Good Bye!")

