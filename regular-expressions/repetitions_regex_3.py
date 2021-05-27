import re

'''
Match a specific number of 
repetitions of a group
'''
laughter_regex = re.compile(r'(Ha){3}')
match_object = laughter_regex.search('He said "HaHaHa"')
print(match_object.group())

# Match three phone numbers in a row
phone_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
match_object = phone_regex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(match_object.group())
