import re

randStr = "412-555-1212"
regex = re.compile(r"([\d]{3})-([\d]{3})-([\d]{4})")
randStr = re.sub(regex, r"(\1)\2-\3" , randStr)
print(randStr)