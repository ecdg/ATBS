''' Using pipe character to match one of several patterns
    as part of the regular expression '''
import re

# Create regular expression object
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')

# Return match object
mo = bat_regex.search('Batmobile lost a wheel')

# Print 'Batmobile'
print(mo.group())

message = 'Batmobile lost a wheel, Batcopter is not a chopper, his name is Batman, not Batbat'

# To find every pattern provided in the regular expession
# Print a list containing all the patterns found
print(bat_regex.findall(message))

# To find an occurence of any of the patterns provided in the regex
mo = bat_regex.search('Batcopter is not a chopper, Batmobile lost a wheel, his name is Batman, not Batbat')

# Print 'Batcopter'
print(mo.group())

# Print the first occurence of a pattern provided in the regex
# Print 'copter'
print(mo.group(1))

# Demonstrate a 'None' return from the search method  
mo = bat_regex.search('Batmotorcycle lost a wheel')
if mo == None:
    print('Batmotorcycle pattern is not found')
