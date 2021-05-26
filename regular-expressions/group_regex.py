''' The program demonstrates finding parts of a pattern
    within a string using regular expression '''
import re

# Create regular expression object
# To identify the phone number pattern
# Also to identify individual groups in the pattern using ()
phone_num_regex_1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Return match object
match_object_1 = phone_num_regex_1.search('My number is 415-555-4242')

# Print the first occurence of the phone number pattern
print(match_object_1.group())

# Print the area code part of the phone number pattern
print(match_object_1.group(1))

# Demonstrates a different phone number pattern to find
phone_num_regex_2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')

# Return match object
match_object_2 = phone_num_regex_2.search('My number is (415) 555-4242')

# Print the first occurence of the phone number pattern
print(match_object_2.group())
