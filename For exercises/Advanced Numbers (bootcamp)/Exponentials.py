# The function pow() takes two arguments, equivalent to x^y. 
# With three arguments it is equivalent to (x^y)%z, but may be more efficient for long integers.

print(pow(2,3)) # 2**3 = 8
print(pow(3,2,5)) # 3**2%5 = 9%5 = 4
print(pow(100000, 144)) # efficient for long integers

# output
# 8
# 4
# 10000000000000000000000000000000000000000000000000000000000000000000000...