import re

# 'wo' can appear once or never appears
bat_regex = re.compile(r'Bat(wo)?man')

match_object = bat_regex.search('The Adventures of Batman')
print(match_object.group())

match_object = bat_regex.search('The Adventures of Batwoman')
print(match_object.group())

match_object = bat_regex.search('The Adventures of Batwowowowoman')
if match_object == None:
    print('Batwowowowoman pattern is not found')

'''
* (asterisk) in the context of regular expressions
means matches zero or more times
'''

# 'wo' can appear zero or more times
bat_regex = re.compile(r'Bat(wo)*man')

match_object = bat_regex.search('The Adventures of Batman')
print(match_object.group())

match_object = bat_regex.search('The Adventures of Batwoman')
print(match_object.group())

match_object = bat_regex.search('The Adventures of Batwowowowoman')
print(match_object.group())

'''
If you need to match an asterisk (*),
escape it with a backslash: \*
'''

'''
A group preceding a plus sign (+) must appear at least once
in a pattern
''' 

bat_regex = re.compile(r'Bat(wo)+man')

match_object = bat_regex.search('The Adventures of Batman')
if match_object == None:
    print('Batman pattern is not found')

match_object = bat_regex.search('The Adventures of Batwoman')
print(match_object.group())

match_object = bat_regex.search('The Adventures of Batwowowowoman')
print(match_object.group())

'''
To match a plus sign (+) in your pattern,
escape it with a backslash: \+
'''
