# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 09:59:16 2018

@author: joshu
"""

import math
import random

evenList = [i*2 for i in range(10)]
for i in evenList:
    print(i)

numList = [1,2,3,4,5]
powerList = [[math.pow(m,2), math.pow(m,3), math.pow(m,4)] for m in numList]

for i in powerList:
    print(i)
print()

multiDList = [[random.randrange(10)]*10 for i in range(10)]

#print(multiDList)

listTable = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i, j)
        
for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" || ")
    print()




