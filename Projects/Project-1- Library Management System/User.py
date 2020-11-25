# -*- coding: utf-8 -*-
from Catalog import Catalog
from Book import Book


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id


class Member(User, Catalog):
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    def issueBook(self, name, days=10):
        pass

    #assume name is unique
    def returnBook(self, name):  # TODO: add calculate fine method
        pass


class Librarian(User, Catalog):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        Catalog.__init__(self)

    def __repr__(self):
        return self.name + self.location + self.emp_id

    def addBook(self, name, author, publish_date, pages):
        book = Book(name, author, publish_date, pages)
        self.different_book_count += 1
        self.books.append(book)
        return book

    def addBookItem(self, book, isbn, rack):
        super()._addBookItem(book, isbn, rack)

    def removeBookItem(self, name, isbn):
        super()._removeBookItem(name, isbn)

    def removeBookFromCatalog(self, name):
        super()._removeBookFromCatalog(name)
