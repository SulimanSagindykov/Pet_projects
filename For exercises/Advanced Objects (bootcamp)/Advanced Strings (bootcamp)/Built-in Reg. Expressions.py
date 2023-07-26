# We can use split() to split the string at a certain element and return a list of the results. 
# We can use partition() to return a tuple that includes the first occurrence of the separator sandwiched between the first half and the end half.

string_1 = 'Hi. This is a ...'
string_2 = 'Everybody'

print(string_1.split('m'))

print(string_1.split('i'))

for i in string_1.split(' '):
    print(i)

print(string_2.partition('y'))
print(string_2.partition('body'))
