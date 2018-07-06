# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:34:41 2018

@author: joshu
"""

# A prime can only be divided by 1 and itself

# Input max prime
# Use a for loop and check if modulus == 0 True

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0: 
            return False
    return True

def get_primes(max_number):
    list_of_primes = []
    
    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    return list_of_primes

max_num_to_check = eval(input("What is the max prime? "))

list_of_primes = get_primes(max_num_to_check)

for prime in list_of_primes:
    print(prime)