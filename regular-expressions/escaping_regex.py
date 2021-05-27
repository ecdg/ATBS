import re

regex = re.compile(r'\+\*\?')
match_object = regex.search('I learned about +*? regex syntax')
print(match_object.group())

# pattern must appear one or more times
regex = re.compile(r'(\+\*\?)+')
match_object = regex.search('I learned about +*?+*?+*?+*?+*? regex syntax')
print(match_object.group())
