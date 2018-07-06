import re

randStr = "F.B.I. I.R.S. CIA"

# Find the number of times #.#.#. occur so anycharacter.anycharacter.anycharacter.
print("Matches :", len(re.findall(".\..\..\.", randStr)))