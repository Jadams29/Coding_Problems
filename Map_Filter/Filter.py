print(list(filter((lambda x: x % 2 == 0), range(1,11))))

import random

# ---------- PROBLEM ----------
# Find the multiples of 98 from a random 100 value list with
# values from 1 and 1000

someList = [random.randrange(1, 1000) for i in range(100)]

mult_of_9 = list(filter((lambda x: (x % 9 == 0)),someList))

print(mult_of_9)