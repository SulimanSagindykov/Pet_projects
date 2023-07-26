# Using the function hex() you can convert numbers into a hexadecimal format
# a*(16)**(n) + b*(16)**(n-1) + ... + c*(16)**(1) + d*(16)**(0) 
# a = 10, b = 11, c = 12, d = 13, e = 14, f = 15

print(hex(16)) # 16 -> 10 = 1*(16)**(1) + 0*(16)**(0) 
print(hex(17)) # 17 -> 11
print(hex(33)) # 33 -> 21
print(hex(79)) # 79 -> 4f = 4*(16)**(1) + 15*(16)**(0) = 64 + 15
print(hex(74)) # 74 -> 4a = 4*(16)**(1) + 10*(16)**(0) = 64 + 10
print(hex(246)) # 246 -> f6

# output
# 0x10
# 0x11
# 0x21
# 0x4f
# 0x4a
# 0xf6