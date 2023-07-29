def factorial(x):

    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

while True:
    try:
        x = int(input('Your Number: '))
        if x >= 0:
            break
        else:
            print('Please enter a positive number')
    except:
        print('Please enter a positive number')


factorial(x)