# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class


class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []

    #Only available to admin
    def _addBook(self, name, author, publish_date, pages):
        book = Book(name, author, publish_date, pages)
        self.different_book_count += 1
        self.books.append(book)
        return book

    #Only available to admin
    def _addBookItem(self, book, isbn, rack):
        book.addBookItem(isbn, rack)

    def searchByName(self, name):
        for book in self.books:
            if name.strip() == book.name:
                return book

    def searchByAuthor(self, author):  # completed
        for book in self.books:
            if author.strip() == book.author:
                return book

    def displayAllBooks(self):
        print('Books in catalog:', self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()

        print('Total Book Count:', c)

    def _removeBookItem(self, name, isbn):
        book = self.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)

    def _removeBookFromCatalog(self, name):
        book = self.searchByName(name)
        self.books.remove(book)
        self.different_book_count -= 1
        del book
