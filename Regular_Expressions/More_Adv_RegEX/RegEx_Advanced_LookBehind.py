import re

# Look Behind
# (?<=expression)

randStr = "1. Bread 2. Apples, 3. Lettuce"

regex = re.compile(r"(?<=\d.\s)\w+")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)

