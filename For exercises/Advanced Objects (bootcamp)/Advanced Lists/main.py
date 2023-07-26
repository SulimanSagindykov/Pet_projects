list_1 = [x for x in range(4)]
list_2 = [x for x in range(4,6)]

list_1.append(list_2)
print(list_1)
# output - [0, 1, 2, 3, [4, 5]]

list_1.extend(list_2)
print(list_1)
# output - [0, 1, 2, 3, [4, 5], 4, 5]

list_1.insert(3, 999) # 3 is an index and 999 is an element
print(list_1)
# output - [0, 1, 2, 999, 3, [4, 5], 4, 5]

list_1.pop()
print(list_1)
# output - [0, 1, 2, 999, 3, [4, 5], 4]

print(list_1.count(999))
# output - 1



# remove
# The remove() method removes the first occurrence of a value
a = [1, 2, 2, 3, 4, 5]
a.remove(2)
print(a)
# output - [1, 2, 3, 4, 5]

# reverse
a.reverse()
print(a)
# output - [5, 4, 3, 2, 1]

# sort
b = [1, 7, 10, 3, 2, 9]
b.sort()
print(b)
b.sort(reverse=True)
print(b)
print(b.sorted())