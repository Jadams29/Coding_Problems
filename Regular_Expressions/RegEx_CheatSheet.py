import re

# if re.search("REGEX", yourString)

# print("Matches :", len(re.findall("REGEX", yourString)))

# regex = re.compile("REGEX")

# yourString = regex.sub("substitution", yourString)

# [ ]    : Match what is in the brackets
# [^ ]   : Match anything but what is in the brackets
# ( )    : Return surrounded submatch
# .      : Match any 1 character or space
# +      : Match any 1 or more of what proceeds
# ?      : Match 0 or 1
# *      : Match 0 or More
# *?     : Lazy match the smallest match
# \b     : Word Boundary
# ^      : Beginning of String
# $      : End of String
# \n     : Match any newline
# \d     : Match any 1 number
# \D     : Match anything but a number
# \w     : Same as putting [a-zA-z0-9_]
# \W     : Same as putting [^a-zA-Z0-9_]
# \s     : Same as putting [\f\n\r\t\v]
# \S     : Same as putting [^\f\n\r\t\v]
# {5}    : Match 5 of what proceeds the curly brackets
# {5,7}  : Match values that are between 5 and 7 in length
# ($m)   : Allow ^ on multiline string

# Use a back reference to substitute what is between the
# bold tags and eliminate the bold tags
# re.sub(r"<b>(.*?)</b>", r"\1", randStr

# Use a look ahead to find all characyers of 1 or more
# with a word boundary, but don't return the word boundary
# re.findall(r"\w+(?=\b)", randStr)

# Use a look behind to find words starting with a number,
# period and space, but only return the word that follows
# re.findall(r"(?<=\d.\s)\w+", randStr)

# Use a negative look behind to only return numbers without
# a $ in front of them
# re.findall(r"(?<!\$)\d+", randStr)



