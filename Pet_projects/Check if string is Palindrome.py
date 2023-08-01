def checker():
    string = '0'
    while True:
        string = input('The string: ')
        if string.isalpha() != True or len(string) <= 1:
            print('Please, enter an alphabetic string with at least two characters!')
        else:
            break
    if string == string[::-1]:
        return 'Yay. The string entered by the user is a palindrome!'
    else:
        return 'The string entered by the user is not a palindrome'
print(checker())