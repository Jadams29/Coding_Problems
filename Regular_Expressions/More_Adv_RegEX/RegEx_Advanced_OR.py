import re

# the | is the OR conditional in regular expressions

randStr = "1. Dog 2. Cat 3. Turtle"
regex = re.compile(r"\d\.\s(Dog|Cat)")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)

print()

newRandStr = "12345 12345-1234 1234 12346-333"
newRegEx = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")
newMatches = re.findall(newRegEx, newRandStr)
for k in newMatches:
    print(k)