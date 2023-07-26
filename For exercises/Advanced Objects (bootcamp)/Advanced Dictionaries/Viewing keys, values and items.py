# By themselves the keys(), values() and items() methods return a dictionary view object. 
# This is not a separate list of items. Instead, the view is always tied to the original dictionary.

dict = {'k1':1, 'k2':2, 'k3':3}

dict_keys = dict.keys()
print(dict_keys)

for i in dict_keys:
    print(i)

try:
    print(dict[1]) # error
except:
    print(dict['k1'])

# output
# dict_keys(['k1', 'k2', 'k3'])
# k1
# k2
# k3
# 1