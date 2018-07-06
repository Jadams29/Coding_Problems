# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 09:54:37 2018

@author: joshu
"""
import random

rand_list = [random.randrange(1,10) for i in range(5)]

for k in rand_list:
    print(k, end=", ")
print()

# This will sort the list
rand_list.sort()

# This will sort the list in reverse
rand_list.reverse()

# Change value at index
rand_list.insert(5,10)

# Remove specific element
rand_list.remove(10)

# Remove item at specific index
rand_list.pop(2)

print(rand_list)

