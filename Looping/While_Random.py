# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:32:06 2018

@author: joshu
"""

import random

random_num = random.randrange(1,51)

i = 1

while(i != random_num):
    i += 1
    
print("FOUND THE RANDOM VALUE: {}".format(random_num))