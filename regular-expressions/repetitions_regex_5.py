import re

'''
Python tries to match the longest possible
string that matches the pattern provided
'''
# regular expressions in Python do greedy matches
# here it matches the first five characters
digit_regex = re.compile(r'(\d){3,5}')
match_object = digit_regex.search('1234567890')
print(match_object.group())

'''
To do a non-greedy match, include
a question mark after the curly braces
'''
# matches the smallest possible string
digit_regex = re.compile(r'(\d){3,5}?')
match_object = digit_regex.search('1234567890')
print(match_object.group())
