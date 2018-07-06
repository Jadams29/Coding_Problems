# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:07:43 2018

@author: joshu
"""

# Problem : Receive miles and convert to kilometers
# Kilometers = miles * 1.60934
# Enter Miles
# 5 miles equals # of kilometers

miles = eval(input("Enter Miles: "))
print("{} miles equals {} kilometers".format(miles, (miles*1.60934)))