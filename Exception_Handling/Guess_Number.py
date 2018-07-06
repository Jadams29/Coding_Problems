# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:57:01 2018

@author: joshu
"""

number = 3
while True:
    try:
        guess = int(input("Please enter a number as your guess: "))
        if (guess == number):
            break
    except ValueError:
        print("You entered something other than a number")
    