# A function used to detect a phone number within a string
# Not using regular expression
def is_phone_number(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

# Test function
message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line'
found_number = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)
        found_number = True
if not found_number:
    print('Could not find any phone numbers.')
