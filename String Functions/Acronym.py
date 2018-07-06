# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:20:11 2018

@author: joshu
"""

information = input("Enter the information to make acronym: ")
temp_list = information.split(" ")

for i in temp_list:
    print(i[0].capitalize(), end='')