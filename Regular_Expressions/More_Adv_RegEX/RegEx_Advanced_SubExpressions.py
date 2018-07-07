import re

# Sub-Expressions
randStr = "412-555-1212 412-555-1213 412-555-1214"
regex = re.compile(r"412-(.{8})")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)

print()
# Multiple sub-Expressions
newRandStr = "My number is 412-555-1212"
newRegex = re.compile(r"412-(.*)-(.*)")
newMatches = re.findall(newRegex, newRandStr)

print(newMatches[0][0])
print(newMatches[0][1])