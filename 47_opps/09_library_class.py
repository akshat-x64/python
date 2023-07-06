class library:
    def __init__(self):
        self.books = []
        self.no_book = 0

    def addbook(self, book):
        self.books.append(book)
        self.no_book = len(self.books)

    def showInfo(self):
        print(f"The library has {self.books} and {len(self.books)}")


l1 = library()
l1.addbook("Akshat")
l1.showInfo()
