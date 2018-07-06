import re

randStr = "Here is \\stuff"

# This will produce no result because how python uses \\
print("Find \\stuff :", re.search("\\stuff", randStr))
print()

# To fix we use rawString because rawString doesnt treat \\ as anything special
print("Find \\stuff :", re.search(r"\\stuff", randStr))
print()