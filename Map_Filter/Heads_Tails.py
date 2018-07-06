# ---------- PROBLEM ----------
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts
# Example Output
# Heads : 46
# Tails : 54

import random

def random_Flip(number):

    list = [random.choice(['H','T']) for i in range(number)]
    print("Heads : ", list.count('H'))
    print("Tails : ", list.count('T'))
    return list

random_Flip(100)