# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:09:06 2018

@author: joshu
"""

import math
import random

# Create a 9x9 multiplication table

# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 2, 4, 6, 8, ...
# 3, 6, 9, 12, ...
# 4, 8, 12, 16, ...
# 5, 10, 15, 20, ...
# 6, 12, 18, 24, ...
# 7, 14, 21, 28, ...
# 8, 16, 24, 32, ...
# 9, 18, 27, 36, ...
#
#
multiplication_table = [[0]*9 for i in range(1,10)]


for i in range(0,9):
    for j in range(0,9):
        multiplication_table[i][j] = ((i+1) * (j+1))

for i in range(9):
    print(multiplication_table[i])

print()
# Using list comprehensions
testing_list = [[i * j for j in range(1,10)] for i in range(1,10)]

print(testing_list)

print()
for row in range(0,9):
    print(testing_list[row])



