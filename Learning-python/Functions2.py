# -*- coding: utf-8 -*-
"""
We would like to use a function to determine a letter grade, given a course average.
We might also like to find out how far that average is from the next higher grade.
"""

################################################################################
# Write a function to determine a letter grade given a final average(float) value.
# It should take as an input parameter a number with which to find the grade.
# It should execute a number of if statements to determine the letter grade.
# It should then return that letter grade without printing.
################################################################################
def get_letter_grade(average):
    result = "?"
    
    if average >= 90:
        result = "A"
    elif average >= 86:
        result = "A-"
    elif average >= 82:
        result = "B+"
    elif average >= 78:
        result = "B"
    elif average >= 74:
        result = "B-"
    elif average >= 70:
        result = "C+"
    elif average >= 66:
        result = "C"
    elif average >= 62:
        result = "C-"
    elif average >= 58:
        result = "D+"
    elif average >= 54:
        result = "D"
    elif average >= 50:
        result = "D-"        
    else:
        result = "F"
    
    return result

################################################################################
# *** Optional Bonus ***
################################################################################
# Write a function to determine the points needed for the next higher letter grade
# given a final average(float) value.
# It should take as an input parameter a number with which to find the next higher
# grade and the points needed to earn it.
# It should execute a number of if statements to determine and print out the higher
# the letter grade and points needed to reach it.
################################################################################

def get_higher_grade(average):

    if average >= 90:
        return 0 # you already earned an "A"
    elif average >= 86:
        return 90 - average
    elif average >= 82:
        return 86 - average
    elif average >= 78:
        return 82 - average
    elif average >= 74:
        return 78 - average
    elif average >= 70:
        return 74 - average
    elif average >= 66:
        return 70 - average
    elif average >= 62:
        return 66 - average
    elif average >= 58:
        return 62 - average
    elif average >= 54:
        return 58 - average
    elif average >= 50:
        return 54 - average       
    else:
        return 50 - average
    

################################################################################
# Main Body of the program
################################################################################
# Write an input statement to get a course final average(float) from the user.
# Call the function to determin the letter grade an print a message with that grade.
# Optionally, call the function to determine the next higher grade.
################################################################################

final_score = float(input("Please enter a final average:"))
print("Congratulations, you earned a/an", get_letter_grade(final_score))
point_bump = get_higher_grade(final_score)
if point_bump > 0:
    print("You need", point_bump, "points to earn a/an", get_letter_grade(final_score+point_bump))