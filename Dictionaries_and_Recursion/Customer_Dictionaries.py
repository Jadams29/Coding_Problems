# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:24:23 2018

@author: joshu
"""

add_info = input("Enter Customer (Yes/No): ")
customers = []

while (add_info == 'y') or (add_info == 'Y'):
    fName, lName = input("Enter Customer Name: ").split()
    customers.append({'fName' : fName, 'lName' : lName})
    add_info = input("Enter Customer (Yes/No): ")

for i in customers:
    print(i['fName'], i['lName'])
