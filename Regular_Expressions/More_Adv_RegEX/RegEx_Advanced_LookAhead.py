import re

# Look Ahead
# (? = expression)

randStr = "One two three four"
regex = re.compile(r"\w+(?=\b)")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)
