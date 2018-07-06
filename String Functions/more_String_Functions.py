# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:26:56 2018

@author: joshu
"""


letter_z = 'z'
num_3 = '3'
a_space = ' '

# Check if all characters are numbers
print("Is z a letter or number: ", letter_z.isalnum())

# Checks if all characters are alphabetical 
print("Is z a letter: ", letter_z.isalpha())

# Check if num_3 is a number
print("Is 3 a number: ", num_3.isdigit())

# Checks if letter_z is lowercase
print("Is z a lowercase: ", letter_z.islower())

# Checks if letter_z is uppercase
print("Is z a uppercase: ", letter_z.isupper())

# Checks if a_space is a space
print("Is a space a space: ", a_space.isspace())

def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False
    

print("Is Pi a float: ",isfloat(3.14))