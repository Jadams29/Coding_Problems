import re

randStr = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"

regex = re.compile(r"(.*)\s(.*)\s(.*)")

matches = re.findall(regex, randStr)
for i in range(3):
    print(matches[0][i])
print()
newRandStr = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
newRegex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|\) )?(\d{3})(-| )?(\d{4}|\d{4}))")
newMatches = re.findall(newRegex, newRandStr)
for k in newMatches:
    print(k[0].lstrip())
