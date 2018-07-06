# Regular Expressions (RegEx) are used to
# 1. Search for a specific string in a large amount of data
# 2. Verify that a string has the proper format (Email, Phone #)
# 3. Find a string and replace it with another string
# 4. Format data into the proper form for importing for example


import re

if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)


theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
    locTuple = i.span()
    print(locTuple)
    print(theStr[locTuple[0]:locTuple[1]])
print()
animalStr = "Cat rat mat pat"

allAnimals = re.findall("[Ccrmfp]at", animalStr)

for i in allAnimals:
    print(i)
print()

# Find anything that starts with letters between  C-M and c-m, ending in at, in animalStr
someAnimals = re.findall("[c-mC-M]at", animalStr)

for i in someAnimals:
    print(i)
print()

anotherAnimals = re.findall("[^Cr]at", animalStr)

for i in anotherAnimals:
    print(i)