dict = {x:y for x,y in zip((f'k{n}'for n in range(1,4)), (f'v{n}' for n in range(1,4)))}
for i in dict.keys():
    print(i)
for i in dict.values():
    print(i)
for i in dict.items():
    print(i)

# output
# k1
# k2
# k3
# v1
# v2
# v3
# ('k1', 'v1')
# ('k2', 'v2')
# ('k3', 'v3')