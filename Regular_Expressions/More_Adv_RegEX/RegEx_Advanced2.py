import re

randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

# Greedy vs Lazy
# Greedy will return <name>Life on Mars</name><name>Freaks and Geeks</name>
# Lazy will return the first instance <name>Life on Mars</name>

# GREEDY
regex_Greedy = re.compile("<name>.*</name>")
matches_Greedy = re.findall(regex_Greedy, randStr)
for j in matches_Greedy:
    print(j)

print()
# LAZY
regex_Lazy = re.compile("<name>.*?</name>")
matches_Lazy = re.findall(regex_Lazy, randStr)
for i in matches_Lazy:
    print(i)