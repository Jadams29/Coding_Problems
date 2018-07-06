# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:08:53 2018

@author: joshu
"""

import random
import math

rand_list = [random.randrange(1,100) for i in range(10)]
print()
print(rand_list)
i = len(rand_list) - 1

while i > 1:
    j = 0
    while j < i:
        if (rand_list[j] > rand_list[j + 1]):
            # swap
            temp = rand_list[j]
            rand_list[j] = rand_list[j + 1]
            rand_list[j + 1] = temp
        j += 1
    i -= 1
print(rand_list)