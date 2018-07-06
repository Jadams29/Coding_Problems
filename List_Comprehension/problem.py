# ---------- PROBLEM ----------
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# You'll have to use a list comprehension in a list comprehension

import random

aList = [y for y in [random.randint(1,1001) for x in range(50)] if y % 9 == 0]

print(aList)


