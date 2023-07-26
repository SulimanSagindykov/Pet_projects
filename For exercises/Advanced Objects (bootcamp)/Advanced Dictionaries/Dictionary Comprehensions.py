dict = {x:x**2 for x in range(6)}
print(dict)

dict = {a:b for a,b in zip('abcd', range(10))}
print(dict)

# zip
for i, y in zip('aabaaba', [1,2,3,4,5,6,7,8,9,10,11]):
    print(i,y)

# output
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# {'a': 0, 'b': 1, 'c': 2, 'd': 3}
# a 1
# a 2
# b 3
# a 4
# a 5
# b 6
# a 7