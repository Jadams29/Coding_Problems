import re

randStr = "doctor doctors doctor's"

regex = re.compile("[doctor]+['s]*")
matches = re.findall(regex, randStr)

for i in matches:
    print(i)

newRandString = '''Just some words
and some more \r
and more
'''
print(newRandString)

newRegex = re.compile("[\w\s]+[\r]?\n")

newMatches = re.findall(newRegex, newRandString)

for m in newMatches:
    print(m)