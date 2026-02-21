class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print("Book issued successfully")
        else:
            print("Book is already issued")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print("Book returned successfully")
        else:
            print("Book was not issued")

    def display_info(self):
        status = "Issued" if self.is_issued else "Available"
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)

if __name__ == "__main__":

    #Create an object (or instance of the Book class)
    book1 = Book(1, "Introduction to Algorithms", "Thomas H Cormen")
    
    # Using object behaviors (using the methods defined in the class)
    book1.display_info()
    book1.issue_book()
    
    book1.display_info()
    book1.return_book()