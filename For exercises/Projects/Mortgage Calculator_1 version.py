import re

class Mortgage():

    def __init__(self):

        variable = True
        start = input('Do you want to start? Yes or No: ').lower()
        
        while variable == True:
            if start.startswith('n') == True:
                break
            else:
                while True:
                    try:
                        loan = int(input('How much is your loan (in dollars)?: '))
                    except:
                        print('Please type a number!')
                    else:
                        break

                while True:
                    try:
                        interest = int(input('What is the interest (in percentage)?: '))
                    except:
                        print('Please type a number!')
                    else:
                        break

                while True:
                    c_interval = input('Please select the compounding interval from the following: Yearly, Monthly, Weekly, and Daily = ')
                    if c_interval.lower() not in ['yearly', 'monthly','weekly','daily']:
                        print('You have made a mistake')
                    else:
                        break

                while True:
                    interval = input('Please select the interval (a fixed term): ').lower()
                    if re.findall(r'\d', interval) == [] or re.findall(r'month|year', interval) == []:
                        print('You have made a mistake. Write xx months/month or xx years/year')
                    else:
                        break

                self.loan = loan
                self.interest = interest
                self.interval = interval
                self.c_interval = c_interval
                variable = False
        

    def total_days(self):

        def m():
            return 30*int(''.join(re.findall(r'\d+', self.interval)))
        
        def y():
            return 30*12*int(''.join(re.findall(r'\d+', self.interval)))
         
        interval_kwords = {'month': m(), 'months' : m(), 'year' : y(), 'years' : y()} 
        for i in interval_kwords.keys():
            if ''.join(re.findall(rf'{i}',self.interval)) == i and re.findall(rf'{i}', self.interval) != []:
                total_days = interval_kwords[i]
                return total_days
                

    def updated_loan(self, total_days, months):

        def yearly():
            updated_loan = self.loan
            years = months//12
            for i in range(years):
                updated_loan += updated_loan*self.interest/100
            return updated_loan

        def monthly():
            updated_loan = self.loan
            for i in range(months):
                updated_loan += updated_loan*self.interest/100
            return updated_loan

        def weekly():
            updated_loan = self.loan
            weeks = total_days//7
            for i in range(weeks):
                updated_loan += updated_loan*self.interest/100
            return updated_loan

        def daily():
            updated_loan = self.loan
            for i in range(total_days):
                updated_loan += updated_loan*self.interest/100
            return updated_loan

        c_interval_dict = {'yearly': yearly(),'monthly': monthly(), 'weekly': weekly(), 'daily': daily()}
        return c_interval_dict[self.c_interval.lower()]
        

class Mortgage_Calculator(Mortgage):
    
    def start(self):
        
        total_days = Mortgage.total_days(self)
        months = total_days//30
        updated_loan = Mortgage.updated_loan(self, total_days, months)
        print(f'Convertation: {self.interval} is {total_days} days')
        print(f'Your calculated loan after the interest is {updated_loan} dollars')
        print(f'Your monthly payment is {updated_loan//months} dollars')
        

print('Welcome to Mortgage Calculator!')

while True:
    calculator = Mortgage_Calculator()
    try:
        calculator.start()
    except:
        break

    end = input('Do you want to try again? Yes or No: ').lower()
    if end.startswith('n') == True:
        break

print('Goodbye. Have a great day!')






    