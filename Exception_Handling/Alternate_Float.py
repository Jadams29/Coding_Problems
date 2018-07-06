# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:18:15 2018

@author: joshu
"""

from decimal import Decimal as D

sum = D(0)

sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("Sum = ", sum)

print("0.1 + 0.1 + 0.1 - 0.3 = ", (0.1 + 0.1 + 0.1 - 0.3))