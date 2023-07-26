text = 'Hello world'
text_l = 'hello world'
text_u = 'HELLO WORLD'
num = '888'
title = 'Hello'

print(text_l.islower()) # Returns True if the string is entirely a lowercase string, False otherwise.
# True

print(text_u.isupper()) # Returns True if the string is entirely an uppercase string, False otherwise.
# True

print(text.islower())
# False because string contains one upper case letter

print(title.istitle()) # Returns True if the string is a title-cased string, False otherwise.
# True because the string doesn't contain a space and starts with a upper case letter

print(text.isalpha()) # Returns True if the string is an alphabetic string, False otherwise.
# False because string contains a space

print(text.isalnum()) # Returns True if the string is an alpha-numeric string, False otherwise.
# False because string contains a space

print(num.isnumeric()) # Returns True if the string is a numeric string, False otherwise.
# True because string contains only numbers

print(num.endswith('8')) # is the same as
print(num[-1] == '8')