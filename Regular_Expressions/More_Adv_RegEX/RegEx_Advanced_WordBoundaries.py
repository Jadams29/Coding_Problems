import re

randStr = "ape at the apex"

# No boundary
# This will return ape from randStr as well as 'ape' from 'apex'
regex = re.compile(r"ape")
matches = re.findall(regex,randStr)
for i in matches:
    print(i)

print()

# Boundary
regex_Bound = re.compile(r"\bape\b")
matches_Bound = re.findall(regex_Bound, randStr)
for j in matches_Bound:
    print(j)