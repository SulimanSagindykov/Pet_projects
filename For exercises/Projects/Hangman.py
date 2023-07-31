import requests
import bs4
import re


class Word():

    def __init__(self):
        x = requests.get(link)
        text = bs4.BeautifulSoup(x.text, 'lxml')
        self.x = x
        self.text = text

    def word(self):
        self.word = self.text.select('#random_word')[0].text.upper()
        return self.word
    
    def definition(self):
        return self.text.select('#random_word_definition')[0].text
    
    def word_show(self, censored_word, letter):
        self.censored_word = censored_word
        self.letter = letter
        if self.letter in self.word:
            pattern = self.letter
            iteration = re.finditer(pattern, self.word)
            for i in iteration:
                index = i.span()[0]
                if index != 0:
                    self.censored_word = self.censored_word[0:index*2 + 1] + self.letter + self.censored_word[index*2+2::]
                else:
                    self.censored_word = self.censored_word[0] + self.letter + self.censored_word[2::]
        return self.censored_word  


class Guess():

    def __init__(self) -> None:
        pass
    
    def guess(self, used_letters):
        self.used_letters = used_letters
        while True:
            letter = input('Guess a Letter: ').upper()
            if letter.isalpha() != True or len(letter) > 1 == True:
                print('Please choose a letter!')
            else:
                if letter in used_letters:
                    print('Please choose another letter!')
                else:
                    used_letters.add(letter)
                    break
        return letter

    def guess_check(self, letter, word):
        self.letter = letter
        self.word = word
        if self.letter in self.word:
            return True
        else:
            return False
        
    def lives(self, result, lives):
        self.result = result
        self.lives = lives
        if self.result == True:
            return f'{self.lives}'
        else:
            return f'{self.lives}-1'
        
    
class Game_on():

    def __init__(self) -> None:
        pass
    
    def start(self):

        game_on = True
        print(f'Welcome to a guessing game: Hangman. You have to a guess a random word generated from this website -> {link}')
        print('You will have 5 lives. Each wrong letter will cost you 1 life')

        while True:
            variable = input("Do you want to start? \nType: 'y' for yes, 'n' for no: ")
            if variable[0] == 'y':
                break
            elif variable[0] == 'n':
                game_on = False
                break
            else:
                print("Please type 'y' or 'n'!")

        while game_on == True:
            used_letters = set()
            true_letters = set()
            lives = 5
            random = Word()
            word = random.word().upper()
            definition = random.definition()
            word_len = len(word)
            censored_word = ' -'*word_len
            for i in word:
                true_letters.add(i)
            print(f"The definition of the word is: {definition}")
            game_process = True

            while game_process == True:
                guess = Guess()
                letter = guess.guess(used_letters)
                guess_check = guess.guess_check(letter, word)
                lives = eval(guess.lives(guess_check, lives))
                print(f'You have {lives} lives left\nUsed Letters: {used_letters}')
                censored_word = random.word_show(censored_word, letter)
                print(f'The Word: {censored_word}\n')
                if (true_letters.difference(used_letters) == set()) == True:
                    print('Congratulations! You have found the word!')
                    break
                elif lives == 0:
                    print(f'Unfortunately, you have no lives left\nThe word was: {word}')
                    break
            
            while True:
                variable = input("\nDo you want to play again? \nType: 'y' for yes, 'n' for no: ")
                if variable[0] == 'y':
                    break
                elif variable[0] == 'n':
                    game_on = False
                    break
                else:
                    print("Please type 'y' or 'n'!\n")

        print('Goodbye! Have a great day ^-^')


link = 'https://randomword.com/'
game = Game_on()
game.start()