import re

# \d : [0-9]  ----> an number 0-9
# \D : [^0-9] ----> not 0-9
# \w : [a-zA-Z0-9_] --> Matches any alphabet (upper/lower) and number (0-9) and (_)
# \W : [^a-zA-Z0-9_] ->
# \s : [\f\n\r\t\v]
# \S : [^\f\n\r\t\v]
#


randStr = "12345"

print("Matches :", len(re.findall('\d{5}', randStr)))

numStr = "123 12345 123456 1234567"
print()
print("Matches :", len(re.findall("\d{5,7}",numStr)))

phNum = "412-555-1212"
print()

if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")
print()

if re.search("\w{2,20}", "Ultraman"):
    print("Is a valid name")
print()

if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("Is Valid")
print()

print("Matches :", len(re.findall("a+", "a as ape bug")))