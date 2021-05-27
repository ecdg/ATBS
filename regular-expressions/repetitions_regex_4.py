import re

# match a range of possible repetitions

# match anywhere between three and five repetitions
# min of three and max of five repetitions
laughter_regex = re.compile(r'(Ha){3,5}')
match_object = laughter_regex.search('He said "HaHaHa"')
print(match_object.group())

match_object = laughter_regex.search('He said "HaHaHaHaHa"')
print(match_object.group())

'''
Anything more than five 'Ha's would result to a match
containing the maximum number of 'Ha's provided in the
regular expression (five 'Ha's): 'HaHaHaHaHa'
'''

match_object = laughter_regex.search('He said "HaHaHaHaHaHaHa"')
print(match_object.group())

# min of zero and max of five matches
laughter_regex = re.compile(r'(Ha){,5}')

# three matches or more
laughter_regex = re.compile(r'(Ha){3,}')
