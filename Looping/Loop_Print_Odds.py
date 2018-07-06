# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:48:07 2018

@author: joshu
"""

# Use for loop to iterate through list from 1 - 21

# Use modulus to check if odd or even

# Print out the odd numbers

for i in range(1, 22):
    if ((i % 2) != 0):
        print("i = ", i)
        
        
newlist = [i for i in range(1,22) if (i %2 != 0)]

print(newlist)