''' The program demonstrates finding parts of a pattern
    within a string using regular expression '''
import re

# Create regular expression object
# To identify the phone number pattern
# Also to identify individual groups in the pattern using ()
phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Return match object
matchObject1 = phoneNumRegex1.search('My number is 415-555-4242')

# Print the first occurence of the phone number pattern
print(matchObject1.group())

# Print the area code part of the phone number pattern
print(matchObject1.group(1))

# Demonstrates a different phone number pattern to find
phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')

# Return match object
matchObject2 = phoneNumRegex2.search('My number is (415) 555-4242')

# Print the first occurence of the phone number pattern
print(matchObject2.group())
