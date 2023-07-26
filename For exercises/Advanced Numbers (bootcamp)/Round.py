# The function round() will round a number to a given precision in decimal digits (default 0 digits). 
# It does not convert integers to floats.

print(round(1.2)) # 1.2 -> 1
print(round(-112)) # -112 -> -122

# print(round(x,-y)). -y is a number of digits, counting from the right, that are rounded
print(round(-112, -1)) # -112 -> 110
print(round(333926, -3)) # 333926 -> 334000
print(round(333926, -2)) # 333926 -> 333900

# print(round(x,y)). y is a number of digits, counting after the dot, that are rounded
print(round(1.2222, 3)) # 1.2222 -> 1.222
import math
print(f'{math.pi} -> {round(math.pi, 3)}') # 3.141592653589793 -> 3.142

# output
# 1
# -112
# -110
# 334000
# 333900
# 1.222
# 3.141592653589793 -> 3.142
