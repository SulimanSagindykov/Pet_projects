import random 

def guess(n):
    random_number = random.randint(1,n)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input('Choose the number between 1 and {}: '.format(n)))
            while guess > n:
                print('Please choose the number in your range')
        except: 
            print('Please type an integer!')
        
        if random_number - 2 < guess < random_number + 2:
            print('You were close ^^ . Try again!'.format(random_number))
        else:
            print('Try again!')
    print('You guessed right')
    print(random_number)

guess(10)
