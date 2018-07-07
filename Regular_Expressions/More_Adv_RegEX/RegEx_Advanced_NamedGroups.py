import re

randStr = "December 21 1974"

regex = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"
matches = re.search(regex, randStr)
print("Month: ", matches.group('month'))
print("Day: ", matches.group('day'))
print("Year: ", matches.group('year'))