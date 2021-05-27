import re

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
match_object = phone_regex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(match_object.group())

match_object = phone_regex.search('My phone number is 555-1234. Call me tomorrow.')
print(match_object.group())

# findall() returns an array with all of the () groups it matches
phone_regex = re.compile(r'(\d\d\d\d(-)?\d\d\d(-)?\d\d\d)')
match_object = phone_regex.findall('My phone numbers are 0912345678 and 0913-234-567')
# prints out the phone numbers
# excluding individual matches of (-)
for i in range(len(match_object)):
  print(match_object[i][0])
  
# prints the array that contains all of 
# the () groups that findall() matches
print(match_object)
  
'''
To include a question mark as part of the 
pattern, use a backslash in front of it: \?
'''
