# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:24:04 2018

@author: joshu
"""

import os
import random
import math

# Creation of a tuple
myTuple = (1,2,3,5,8)

# print the first element in tuple
print("1st value: ", myTuple[0])
print()
print("1st value: {}".format(myTuple[0]))
print()

# Slices of Tuple
print("Slice of myTuple[0:3]: ", myTuple[0:3])
print()
print("Slice of myTuple[0:3]: {}".format(myTuple[0:3]))
print()

# Find the length of a tuple
print("Tuple length: ", len(myTuple))
print()
print("Tuple length: {}".format(len(myTuple)))
print()

# Concat Tuples
moreFibs = myTuple + (13,21,34)
print("Concat tuple: ", moreFibs)
print()
print("Concat tuple: {}".format(moreFibs))


# Check if a value exists in a tuple
print("Check if 32 in Tuple: ", 32 in moreFibs)
print()
print("Check if 32 in Tuple: {}".format(32 in moreFibs) )


# Iterate over tuple
for i in moreFibs:
    print(i)

# Convert a list into a tuple
aList = [55,89,144]
aTuple = tuple(aList)

# Convert a tuple into a list
aList = list(aTuple)

print(aTuple)
# Find the Min/Max of a tuple
print("Min : {} \nMax : {}".format(min(aTuple), max(aTuple)))






