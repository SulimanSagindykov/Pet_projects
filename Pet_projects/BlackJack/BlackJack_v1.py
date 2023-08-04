#Input
#PLAN
# Welcome
# show balance
# Create Deck
# deal 4 cards
# show cards 
# hit or stay for player
# if hit check whether not over 21 
# again hit or pass for player 
# if over 21, player lose
# if stay and under 21, dealer's turn
# while loop (True)
# hits for dealer
# if under 21 and under player_value, continue hitting
# if over 21, player won
# show balance
# ask if want to bet again (play again)

import random
value_of_cards = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8,9:9, 10:10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
class Bank():
    def __init__(self, chips):
        self.chips = chips
        print(f'Your current balance is: {self.chips}')
    
    def bet(self):
        while True:
            try:
                self.player_bet = int(input('Place your bet: '))
                if self.player_bet > self.chips:
                    print("You don't have enough chips")
                    pass
                else:
                    self.chips -= self.player_bet
                    print(f'Your bet has been placed. Your current balance is: {self.chips}')
                    break
            except:
                print('Please choose the number of chips!!!')

class Deck():
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        numbers = ['Ace', 'Jack', 'Queen', 'King',2,3,4,5,6,7,8,9,10]
        for i in suits:
            for x in numbers:
                deck_of_cards.append([x,i])
        random.shuffle(deck_of_cards)
        
    def deal(self,who):
        if who == 'Player':
            player_cards.append(deck_of_cards.pop())
        if who == 'Dealer':
            dealer_cards.append(deck_of_cards.pop())

class Hit_or_Stay(Deck):
    def __init__(self):
        pass
    def f(self):
        while True:
            try:
                variable3 = input('Do you want to "Hit" or "Stay"?: ')
                if variable3 == 'Hit':
                    self.deal('Player')
                    print(f'You recieved: {player_cards[-1]}')
                    return 'Hit'                   
                elif variable3 == 'Stay':
                    print("You chose to 'Stay'")
                    return 'Stay'
                else:
                    print("Please choose either 'Hit' or 'Stay'")
            except:
                print("Please choose either 'Hit' or 'Stay'")
    def checker(self,who):
        global dealer_value
        global player_value
        if who == 'Player':
            player_value = player_value + value_of_cards[player_cards[-1][0]]
        else:
            dealer_value = dealer_value + value_of_cards[dealer_cards[-1][0]]

        


print('Welcome')
variable1 = Bank(100)
variable4 = True
while variable4 == True:
    deck_of_cards = []
    player_cards = []
    dealer_cards = []
    variable1.bet()
    variable2 = Deck()
    for i in range(1,3):
        for x in ['Player', 'Dealer']:
            variable2.deal(x)
    print(f"Player's cards are {player_cards}")
    print(f"Dealer's cards are {dealer_cards[0]}, ???")
    print('\nPlayer starts')
    Game = True
    while Game == True:
        player_value = value_of_cards[player_cards[0][0]] + value_of_cards[player_cards[1][0]]
        dealer_value = value_of_cards[dealer_cards[0][0]] + value_of_cards[dealer_cards[1][0]]
        while Game == True:
            choice = Hit_or_Stay()
            if choice.f() == 'Hit':
                print(f"Player's cards are {player_cards}")
                choice.checker('Player')
                print(player_value)
                if player_value > 21:
                    print('Player lost the bet')
                    Game = False
                    break
                else:
                    pass
            else:
                print("\nDealer's Turn")
                break
        while Game == True:
            variable2.deal('Dealer')
            print(f'Dealer recieved: {dealer_cards[-1]}')
            print(f"Dealer's cards are {dealer_cards[0]}, ???, {dealer_cards[2::]}")
            choice.checker('Dealer')
            if dealer_value > player_value and dealer_value <= 21:
                print("\nDealer has won!!!")
                print(f"Dealer's cards are {dealer_cards}\nPlayer's cards are {player_cards}")
                Game = False
                break
            elif dealer_value > 21:
                print('\nPlayer has won!!!')
                print(f"Player's cards are {player_cards}\nDealer's cards are {dealer_cards}")
                variable1.chips += 2 * variable1.player_bet
                Game = False
                break
            else:
                pass
    while True:
        try:
            print(f'Your current balance is: {variable1.chips}')
            variable3 = input('Would you like to play again? Yes or No: ')
            if variable3 == 'Yes':
                break
            elif variable3 == 'No':
                print('Thank you for the game! See you soon.')
                variable4 = False
                break
            else:
                print('Please choose either Yes or No')
        except:
            print('Please choose either Yes or No')