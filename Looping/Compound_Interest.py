# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:10:26 2018

@author: joshu
"""

# Have the user enter their investment amount and expected interest

# Each year their investment will increase by their investment + their 
#    investment * interest rate

# Print out the earnings after a 10 year period


money, interest_rate = input("Please enter your investment amount and \
                                                   your expected interest: ").split(" ")
money = float(money)
interest_rate = float(interest_rate)

for i in range(1,11):
    money = money + (money * interest_rate)
    print("For year {}, your investment amount was {:.2f}: ".format(i, money))