import re

# 'wo' can appear once or never appears
bat_regex = re.compile(r'Bat(wo)?man')

mo = bat_regex.search('The Adventures of Batman')
print(mo.group())

mo = bat_regex.search('The Adventures of Batwoman')
print(mo.group())

mo = bat_regex.search('The Adventures of Batwowowowoman')
if mo == None:
    print('Batwowowowoman pattern is not found')
