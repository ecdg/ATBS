import re

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
match_object = phone_regex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(match_object.group())

match_object = phone_regex.search('My phone number is 555-1234. Call me tomorrow.')
print(match_object.group())

'''
To include a question mark as part of the 
pattern, use a backslash in front of it: \?
'''
