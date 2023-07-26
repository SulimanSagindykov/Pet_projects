a = set()

# add
a.add('1')
a.add(1)
print(a)
# output - {1, '1'}


# clear
a.clear()
print(a)
# output - set()


# copy
b = {1,2,3}
a = b.copy()
print(a)
# output - {1, 2, 3}
a.add(4)
print(a)
# output - {1, 2, 3, 4}


# difference
# difference returns the difference of two or more sets
a = {1, 2, 3, 4, 5}
b = {1 ,2, 3, 6}
print(a.difference(b))
print(b.difference(a))
# output - {4}


# difference_update
# the method returns set1 after removing elements found in set2
a = {10, 20, 30}
b = {20, 40, 50}
a.difference_update(b)
print(a)
# output - {10, 30}

a = {10, 20, 30}
b = {20, 40, 50}
b.difference_update(a)
print(b)
# output - {40, 50}


# symmetric_difference and symmetric_update
a = {1, 2, 3, 4, 5}
b = {1 ,2, 3, 6}
print(a.symmetric_difference(b))
# output - {4, 5, 6}
a.symmetric_difference_update(b)
# result -> a = {4, 5, 6}



# discard
# Removes an element from a set if it is a member. If the element is not a member, do nothing.
a = {1,2,3,4}
a.discard(3)
print(a)
# output - {1, 2, 4}
a.discard(5)
print(a)
# output - {1, 2, 4}


# intersection and intersection_update
# Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)
s1 = {1,2,3}
s2 = {2,1,4,6}
print(s1.intersection(s2))
# output - {1, 2}

s1.intersection_update(s2)
print(s1, s2)
# output - {1, 2} {1, 2, 4, 6}

s2.intersection_update(s1)
print(s2, s1)
# output - {1, 2} {1, 2}


# isdisjoint
# This method will return True if two sets have a null intersection.
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s1.isdisjoint(s2))
# output - False
print(s3.isdisjoint(s1))
# output - True


# issubset 
# This method will report whether one set is a subset of another.
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s2.issubset(s1))
# output - False
print(s1.issubset(s2))
# output - True


# issuperset
# This method will report whether one set is a superset of another.
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s2.issuperset(s1))
# output - True


# union
# Returns the union of two sets (i.e. all elements that are in either set.)
s1 = {1,2,3}
s2 = {2,1,4,6}
print(s1.union(s2))
# output - {1, 2, 3, 4, 6}
print(s1)
# output - {1, 2, 3}

# update
# Update a set with the union of itself and others.
s1 = {1,2,3}
s2 = {2,1,4,6}
s1.update(s2)
print(s1)
# output - {1, 2, 3, 4, 6} 

