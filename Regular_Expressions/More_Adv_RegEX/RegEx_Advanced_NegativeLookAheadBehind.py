import re

# Negative look ahead, look behind

# (?!expression)    : Negative Look Ahead
# (?<!expression)   : Negative look Behind

randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex = re.compile(r"(?<!\$)\d+")
matches = re.findall(regex, randStr)
print(len(matches))
matches = [int(i) for i in matches]

from functools import reduce

print("Total Items {}".format(reduce((lambda x, y: x + y), matches)))