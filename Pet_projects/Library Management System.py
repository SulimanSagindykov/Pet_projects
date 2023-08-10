import time
tab = ' '*12

class Library():

    def __init__(self, books):
        self.books = books

    def display(self):
        print(f'''
        ==========Available Books==========
              ''')
        for i,n in self.books.items():
            if n == 'Free':
                print(tab,i)

    def borrowed_book(self, book):
        self.books[book] = 'Not Free'
    
    def returned_book(self, book):
        self.books[book] = 'Free'


class Reader():

    def __init__(self, user, library):
        self.user = user
        self.library = library
        self.user_books = []

    def borrow_book(self):
        print('What is the book you wish to borrow?')
        borrowed_book = input('Name: ')

        if borrowed_book in self.library.books.keys():
            if self.library.books[borrowed_book] == 'Free':
                self.user_books.append(borrowed_book)
                self.library.borrowed_book(borrowed_book)
                print('Book has been successfully borrowed!')
            else:
                print('It has already been borrowed and is currently not free ')
        else:
            print('There is no such book in the library')


    def return_book(self):
        print('What is the book you wish to return?')
        return_book = input('Name: ')
        if return_book in self.user_books:
            for i in self.user_books:
                if i == return_book:
                    self.user_books.remove(i)
            self.library.returned_book(return_book)
            print('Book has been successfully returned!')
        else:
            print('There is no such book in the list of your borrowed books')
        
    def books(self):
        if self.user_books != []:
            print(f'''
            ==========List of Your Books==========
              ''')
            for i in self.user_books:
                print(tab, i)
        else:
            print("User doesn't have any borrowed books")

    
def create_libary():
    books = {
       'The Twilight Saga': 'Free',
       'Harry Potter': 'Free',
       'The Alchemist': 'Free',
       'The Da Vince Code': 'Free',
       'Lord of the Flies': 'Free'
   }

    library = Library(books)
    user = Reader('Suliman', library)

    while True:
        time.sleep(2)
        print('''
           ==========LIBRARY MENU===========
           1. Display Available Books
           2. Borrow a Book
           3. Return a Book
           4. View Your Books
           5. Exit'''
             )
        
        try:
            option = int(input('\nType the option from 1 to 5: '))
        
        except:
            print('\n\n\nYou did not type the number')
        
        else:
            if option == 1:
                library.display()

            elif option == 2:
                user.borrow_book()
            
            elif option == 3:
                user.return_book()

            elif option == 4:
                user.books()

            elif option == 5:
                print('Goodbye! Have a great day!')
                break
            
            else:
                print('\n\n\nYou did not type a number between 1 and 5')
            
create_libary()


