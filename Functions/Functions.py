# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:09:31 2018

@author: joshu
"""


def add_numbers(num1, num2):
    return num1+num2

def assign_name():
    name = 'Doug'
    
gbl_name = 'Sally'

def change_name():
    global gbl_name
    gbl_name = 'Sammy'
    
change_name()

print(gbl_name)

def get_sum(num1, num2)