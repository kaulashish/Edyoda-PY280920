# -*- coding: utf-8 -*-
from Catalog import Catalog
from Book import Book


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id


class Librarian(User, Catalog):
    lended_book_data = {}

    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        Catalog.__init__(self)
        self.emp_id = emp_id

    def __repr__(self):
        return self.name + self.location + self.emp_id

    def addBook(self, name, author, publish_date, pages):
        return super()._addBook(name, author, publish_date, pages)

    def addBookItem(self, book, isbn, rack):
        super()._addBookItem(book, isbn, rack)

    def removeBookItem(self, name, isbn):
        super()._removeBookItem(name, isbn)

    def removeBookFromCatalog(self, name):
        super()._removeBookFromCatalog(name)
        Catalog.different_books_count = self.different_book_count

    def displaylendedbooks(self):
        if len(Librarian.lended_book_data.items()) == 0:
            print('No books lended\n')
        else:
            print('\n')
            for key, value in Librarian.lended_book_data.items():
                print(key, ':')
                print(*value, sep=', ')
            print('\n')


class Member(User, Catalog):
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.bookitems = []  #contains book isbn
        self.issuedbookcount = 0
        self.booksissued = []  #contains the books that are issued

        # the following variables will enable us to use the Catalog() methods.
        self.different_book_count = super().different_books_count
        self.books = super().books

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    def issueBook(self, name, days=10):
        try:
            book = super().searchByName(name)
            isbn = str(book.book_item[0])
            #check if member already has the book he is trying to issue.
            # if len(self.bookitems) != 0:
            for i in self.booksissued:
                if len(self.bookitems) > 0 and i[0] == book:
                    print(
                        f"Book '{name}' already issued before. Please return the book before issuing it again."
                    )
                    return

            # logic for issuebook() ->
            bookitem = book.searchBookItem(isbn)
            book.removeBookItem(bookitem)
            self.bookitems.append(isbn)
            self.issuedbookcount += 1
            self.booksissued.append((book, isbn))
            # make dict value as tuples in list
            if book not in Librarian.lended_book_data.keys():
                Librarian.lended_book_data[book] = []
                Librarian.lended_book_data[book].append(
                    (bookitem.isbn, bookitem.rack))
            else:
                Librarian.lended_book_data[book].append(
                    (bookitem.isbn, bookitem.rack))
            print(
                f"'{name}' by {book.author} has been issued to {self.name} for {days} days"
            )

        except IndexError:  #exception raised when book to be issued has no relative items.

            # check if member already has the book he is trying to issue.
            if len(self.bookitems) != 0:
                if book in self.booksissued:
                    print(
                        "Book already issued before. Please return the book before issuing it again."
                    )
            else:
                print(
                    f"Sorry {self.name}, All the books by the name '{name}' have been issued."
                )

    #assume name is unique
    def returnBook(self, name):
        try:
            book = super().searchByName(name)
            isbn = list(filter(lambda x: x[0] == book, self.booksissued))[0][1]

            #checking for correlation between self.bookissued and
            #Library.lended_book_data to extract rack value.
            for i in self.booksissued:
                if i[0] == book:
                    for j in Librarian.lended_book_data.get(book):
                        if j[0] == isbn:
                            rack = j[1]

            #return book and update member variables.
            Catalog._addBookItem(self, book, isbn, rack)
            print(f"Book '{book}' returned.\n")
            #updating variables :->
            self.booksissued.remove((book, isbn))
            self.issuedbookcount -= 1
            self.bookitems.remove(isbn)

            #updating Librarian.lended_book_data
            for i in list(Librarian.lended_book_data.keys()):
                #remove individual lended bookitem data from dictionary.
                try:
                    lis = Librarian.lended_book_data.get(book)
                    for j in lis:
                        if isbn == j[0]:
                            Librarian.lended_book_data[book] = list(
                                filter(lambda x: x[0] != isbn, lis))
                            # remove book from dictionary if all the bookitems are returned.
                            if len(Librarian.lended_book_data.get(book)) == 0:
                                Librarian.lended_book_data.pop(i)
                except TypeError:
                    return

        except IndexError:
            print(f"{self.name},'{book}' is not in your inventory.\n")

    def displayissuedbooks(self):
        if len(self.booksissued) > 0:
            print(f'\nBooks issued by {self.name} : \n')
            for i in self.booksissued:
                print(*i, sep=' -> ')
        else:
            print('\nNo books issued.\n')
