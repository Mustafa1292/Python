# -*- coding: utf-8 -*-

def is_vowel(letter): # determine if letter is a vowel
    return letter.upper() in 'AEIOU' # if the letter is a vowel return True


def has_vowel(word): # determine if a word has a vowel in it
    for letter in word: # Loop through all the letters
        if is_vowel(letter): # See if a letter is a vowel
            return True # If so, return True, "has a vowel" is True
    # After looking through all the letters in the word
    return False # we found no vowel, so the word does not have a vowel


def find_vowel(word): # find the vowel in a word
    for letter in word: # Loop through all the letters
        if is_vowel(letter): # See if a letter is a vowel
            return word.find(letter) # If so, return the index of where it is
    return -1


def translate(word):  
    if is_vowel(word[0]): # The word starts with a vowel (Rule #1)
        # add way to the end of the word
        return word + 'way'
    elif has_vowel(word): # The word must have a vowel that is not the first letter (Rule #3)
        index = find_vowel(word) # Find the index of the vowel
        result = word[index:] + word[:index] + "ay"
        if word[0].isupper(): # The first letter is in upper case
            result = result.lower().capitalize() # Fix the caps
        return result # return the converted word
    else:  # The word contains no vowel (Rule #2)
        # add way to the end of the word
        return word + 'way'

# Main body of the program begins here
print("This program will translate a word from English to Pig Latin.")

choice = 'Y' # Initialize the looping variable
while choice.upper() == 'Y': #Loop as long as the user says Yes
    word = input("Please enter a word: ") # get a word
    print(word, "becomes", translate(word)) # translate it
    choice = input("Would you like another word? (Y/N) ")

print("Ankthay ouyay!")