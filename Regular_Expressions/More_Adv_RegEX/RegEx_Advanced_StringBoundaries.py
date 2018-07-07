import re

# ^  :  Indicates the beginning of the string
# $  :  Indicates the end of the string

# Match everything at the beginning of a string
randStr = "Match everything up to @"
regex = re.compile(r"^.*[^@]")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)

print()

randStr1 = "@ Get this string"
regex_End = re.compile(r"[^@\s].*$")
matches_End = re.findall(regex_End, randStr1)
for j in matches_End:
    print(j)

print()

multi_Line = '''Ape is big
Turtle is slow
Cheetah is fast
'''
regex_Multi = re.compile(r"(?m)^.*?\s")
matches_Multi = re.findall(regex_Multi, multi_Line)
for k in matches_Multi:
    print(k)