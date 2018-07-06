# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:43:03 2018

@author: joshu
"""

i = 1

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if ( i == 15):
        break
    
    print("Odd : " , i)
    i += 1
    