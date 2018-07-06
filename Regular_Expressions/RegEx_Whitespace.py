import re

randStr = '''This is a long
string that goes
on for many lines
'''

print(randStr)

regex = re.compile("\n")

randStr = regex.sub(" ", randStr)

print(randStr)

# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab
