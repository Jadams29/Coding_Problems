import re


# ---------- PROBLEM ----------
# Match email addresses
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

# \d : [0-9]  ----> an number 0-9
# \D : [^0-9] ----> not 0-9
# \w : [a-zA-Z0-9_] --> Matches any alphabet (upper/lower) and number (0-9) and (_)
# \W : [^a-zA-Z0-9_] ->
# \s : [\f\n\r\t\v]
# \S : [^\f\n\r\t\v]

randStr = "db@aol.com m@.com @apple.com db@.com"
print("Matches: ", len(re.findall("\w{1,20}[._%+-][@]\w{2,20}[.-]\.\w{2,3}", randStr)))

print("Email Matches: ", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", randStr)))




