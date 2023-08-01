# p.s. that's the first ever project I did. (did it entirely on my own without cheating = looking at others' code, etc.)
# spent a significant amount of time

# Board
one = '     |     |     '
two_2_8_14 = '     |     |     '
three = '     |     |     '
four = '-----------------'
five = '     |     |     '
six_2_8_14 = '     |     |     '
seven = '     |     |     '
eight = '-----------------'
nine = '     |     |     '
ten_2_8_14 = '     |     |     '
eleven = '     |     |     '
list_board = [one,two_2_8_14,three,four,five,six_2_8_14,seven,eight,nine, ten_2_8_14,eleven]
d = {1: 2, 2: 8, 3: 14, 4:2, 5:8, 6:14, 7:2,8:8,9:14}

def board_f():
    for i in list_board:
        print(i)

# Choose X or O
def choice():
    variable1 = False
    while variable1 == False:
        Player1 = input("Player 1: Do you want to be X or O? ")
        if Player1 == 'X':
            print('Player 1 is Player X. Player 2 is Player O')
            variable1 = True
        elif Player1 == 'O':
            print('Player 1 is Player O. Player 2 is Player X')
            variable1 = True
        else:
            print('Please choose either X or O: ')
    return variable1
# Ready? 
def ready():
    variable2 = False
    while variable2 == False:
        n = input('Are you ready to play? Enter Yes or No: ')
        if n == 'Yes' or n == 'No':
            variable2 = True
            return n
        else:
            print('Please choose either Yes or No: ')

# Choose Position
def choose():
    range_1 = [1,2,3,4,5,6,7,8,9]
    range_2 = ['1','2','3','4','5','6','7','8','9']
    variable3 = False
    while variable3 == False:
        x = input('Choose your next position (1-9): ')
        if x in range_1 or x in range_2:
            return x
        else:
            print('Please choose the number from 1 to 9: ')
            
        
# Position of X or O
list = [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ']
list9 = [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ']
list5 = [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ']
list1 = [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ']
def position(marker, posit):
    d = {1: 2, 2: 8, 3: 14, 4:2, 5:8, 6:14, 7:2,8:8,9:14}
    global list_board
    global list9
    global list5
    global list1
    if posit in range(1,4):
        if list9[d[posit]] == list[d[posit]]:
            list9[d[posit]] = marker
            list_board[9] = ''.join(list9)
            return board_f()
        else:
            return 'A'
    elif posit in range(4,7):
        if list5[d[posit]] == list[d[posit]]:
            list5[d[posit]] = marker
            list_board[5] = ''.join(list5)
            return board_f()
        else:
            return 'A'
    else:
        if list1[d[posit]] == list[d[posit]]:
            list1[d[posit]] = marker
            list_board[1] = ''.join(list1)
            return board_f()
        else:
            return 'A'

# Who Won?
def win_check():
    if list_board[1][2] == list_board[1][8] == list_board[1][14] == 'X' or list_board[5][2] == list_board[5][8] == list_board[5][14] == 'X' or list_board[9][2] == list_board[9][8] == list_board[9 ][14] == 'X' or list_board[1][2] == list_board[5][2] == list_board[9][2] == 'X' or list_board[1][8] == list_board[5][8] == list_board[9][8] == 'X' or list_board[1][14] == list_board[5][14] == list_board[9][14] == 'X' or list_board[1][2] == list_board[5][8] == list_board[9][14] == 'X' or list_board[1][14] == list_board[5][8] == list_board[9][2] == 'X':
        print('Player X has won!')
        return ''
    elif list_board[1][2] == list_board[1][8] == list_board[1][14] == 'O' or list_board[5][2] == list_board[5][8] == list_board[5][14] == 'O' or list_board[9][2] == list_board[9][8] == list_board[9 ][14] == 'O' or list_board[1][2] == list_board[5][2] == list_board[9][2] == 'O' or list_board[1][8] == list_board[5][8] == list_board[9][8] == 'O' or list_board[1][14] == list_board[5][14] == list_board[9][14] == 'O' or list_board[1][2] == list_board[5][8] == list_board[9][14] == 'O' or list_board[1][14] == list_board[5][8] == list_board[9][2] == 'O':
        print('Player O has won!')
        return ''

    
# draw
def draw():
    if (list9[2] == 'X' or list9[2] == 'O') and (list9[8] == 'X' or list9[8] == 'O') and (list9[14] == 'X' or list9[14] == 'O') and (list5[8] == 'X' or list5[8] == 'O') and (list5[2] == 'X' or list5[2] == 'O') and (list5[14] == 'X' or list5[14] == 'O') and (list1[8] == 'X' or list1[8] == 'O') and (list1[2] == 'X' or list1[2] == 'O') and (list1[14] == 'X' or list1[14] == 'O'):
        print('Draw!')
        return 'draw'
    
# playing again?
def again():
    again_variable = False
    variable4 = False
    while variable4 == False:
        play_variable = input('Do you want to play again? ')
        if play_variable == 'Yes':
            again_variable = True
            variable4 = True
        elif play_variable == 'No':
            variable4 = True
        else:
            variable4 = False
    return again_variable

print('Welcome to Tic Tac Toe!')
Game_variable = False
logic_variable = False
choice_variable = ["X", "O"] * 10
while Game_variable == False:
    if choice() == True and ready() == 'Yes':
        print('')
    else:
        Game_variable = True
    while logic_variable == False:
        board_f()
        p = position(choice_variable[0], int(choose()))
        if p == 'A':
            print('\n'*10)
            print('Please choose only an empty boxes!')
        elif win_check() == '' or win_check() == 'X' or draw() == 'draw':
            logic_variable = True
        else:
            choice_variable[0] = choice_variable.pop()[0]
            print('\n'*10)
    if again() == False:
        Game_variable = True
print('Game Over')
