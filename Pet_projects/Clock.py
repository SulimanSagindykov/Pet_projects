import time
import re

class Process():
    def __init__(self) -> None:
        pass

    def current_time(self):
        return time.ctime()

    def timer(self, number, unit):
        self.unit = unit
        self.number = eval(number)

        if self.unit == 'minute' or self.unit == 'minutes':
            return self.number*60
        if self.unit == 'second' or self.unit == 'seconds':
            return self.number
        if self.unit == 'hour' or self.unit == 'hours':
            return self.number*(pow(60,2))
        
    def input_(self, x):
        self.x =x

        
class Clock:
    def __init__(self):
        calculations = Process()
        print('Clock')
        clock_on = ''
        question_1 = 'Do you want to start? (Enter y for yes or n for no): '
        game_start = input(question_1)
        while game_start not in ['y','n']:
            game_start = input(question_1)

        if game_start == 'y':
            clock_on = True
        else:
            pass

        while clock_on == True:
            question_2 = '\n\nWhat do you want to do?\n1 -> Check your current time\n2 -> Put a timer\n3 -> Exit\nType either 1, 2, or 3: '
            game_chocie = input(question_2)
            while game_chocie not in ['1','2','3']:
                game_chocie = input(question_2)
            
            if game_chocie == '1':
                print('\n\nYour current time is: ', calculations.current_time())
            
            elif game_chocie == '2':
                print('\n\nTimer!')
                pattern = 'minutes|minute|hours|hour|second|seconds'
                condition1 = False

                while condition1 == False or condition2 == False:
                    time_ = input('Setting timer for (amount of time + unit -> hours/minutes/seconds, e.g. 20 minutes)\n: ')
                    number = re.findall('\d+',time_)
                    unit = re.findall(pattern,time_)
                    condition1 = number != [] and len(number) == 1
                    condition2 = unit != [] and len(unit) == 1
                
                number.extend(unit)
                time_in_seconds = calculations.timer(number[0], number[1])

                for i in range(time_in_seconds):
                    print(f'Time: {time_in_seconds - i} second(s)')
                    time.sleep(1)
                    print('\033[A                     \033[A')
                    
            else:
                break

        print('Goodbye! Have a great day!')

x = Clock()