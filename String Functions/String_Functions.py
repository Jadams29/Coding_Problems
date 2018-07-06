# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:02:14 2018

@author: joshu
"""

rand_string = "   this is an important string     "



# Remove whitespace from the left side of the string
rand_string = rand_string.lstrip()

# Remove whitespace from the right side of the string
rand_string = rand_string.rstrip()

# Remove all whitespace from the string
rand_string = rand_string.strip()

# Capitalize the first character
print("rand_string.capitalize(), should capitalize the first character: ",rand_string.capitalize())

# Make the string all uppercase
print("rand_string.upper(), should make all characters uppercase: ",rand_string.upper())

# Make the string all lowercase
print("rand_string.lower(), should make all characters lowercase: ",rand_string.lower())

# Print a list as a string
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

# Convert a string into a list
a_list2 = rand_string.split()
print(a_list2)

# Number of occurances of something
print("How many is in rand_string: ", rand_string.count('is'))
print("Where is the string : ", rand_string.find("string"))

# Replace a substring with something
print(rand_string.replace("an ", "a kind of "))
