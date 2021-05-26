''' The program demonstrates finding a phone number
    within a string using regular expression '''
import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line'

# Create regular expression object
# To identify the pattern
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# To find the first occurence of the phone number pattern
matchObject = phoneNumRegex.search(message)
print(matchObject.group())

# To find every occurence of the phone number pattern
print(phoneNumRegex.findall(message))
