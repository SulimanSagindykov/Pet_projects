# Using the function bin() you can convert numbers into their binary format
# x is either 1 or 0
# 1*(2)**(n) + x*(2)**(n-1) + ... + x*(2)**(1) + x*(2)**(0)

print(bin(23)) # 23 -> 10111 = 1*(2)**(4) + 0*(2)**(3) + 1*(2)**2 + 1*(2)**1 + 1*(2)**0
print(bin(103)) # 23 -> 1100111

#output
# 0b10111
# 0b1100111