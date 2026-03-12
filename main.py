class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has already been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
  
    def addBook(self,book):
        self.booklist.append(book)
        print(f"Book '{book}' has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)
        print(f"Book '{book}' has been returned")

if __name__=='__main__':
    book=Library(['Dork Diaries', 'Hunger games', 'Girl of Ink and Stars', 'The Hate You Give', 'Noughts and Crosses','Diary of A Wimpy Kid','Harry Potter'],"Book Lover")

    while True:
        print(f"Welcome to the {book.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Exit")
        user_choice=input()
        
        if user_choice not in ['1','2','3','4','5']:
            print("please enter a valid option")
            continue
        if user_choice=='1':
            book.displayBooks()

        elif user_choice=='2':
            book_name=input("Enter the name of the book you want to lend: ")
            user_name=input("Enter your name: ")
            book.lendBook(user_name,book_name)

        elif user_choice=='3':
            book_name=input("Enter the name of the book you want to add: ")
            book.addBook(book_name)

        elif user_choice=='4':
            book_name=input("Enter the name of the book you want to return: ")
            book.returnBook(book_name)
        elif user_choice=='5':
            print("Thank you for using the library. Have a great day!")
            exit()