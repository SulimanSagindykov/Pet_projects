def factorial(x):

    if x == 0:
        print(1)
    else:
        print(x * factorial(x-1))

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