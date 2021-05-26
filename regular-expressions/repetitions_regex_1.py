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
