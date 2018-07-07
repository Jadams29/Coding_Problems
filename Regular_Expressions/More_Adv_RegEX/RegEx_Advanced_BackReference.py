import re

randStr = "The cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+\1")
matches = re.findall(regex,randStr)
print("Matchs : ", len(matches))
for i in matches:
    print(i)
print()

newRandStr = "<a href='#'><b>The Link</b></a>"
print("new rand string before: ", newRandStr)
newRegex = re.compile(r"<b>(.*?)</b>")
newRandStr = re.sub(newRegex, r'\1', newRandStr)
print("new rand string after:  ", newRandStr)
