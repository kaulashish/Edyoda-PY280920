# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

# catalog = Catalog()

# b = catalog.addBook('Shoe Dog', 'Phil Knight', '2015', 312)
# catalog.addBookItem(b, '123hg', 'H1B2')
# catalog.addBookItem(b, '124hg', 'H1B4')
# catalog.addBookItem(b, '125hg', 'H1B5')

# b = catalog.addBook('Moonwalking with Einstien', 'J Foer', '2017', 318)
# catalog.addBookItem(b, '463hg', 'K1B2')
# catalog.addBookItem(b, '464hg', 'K1B3')

# catalog.displayAllBooks()

# # m1 = Member("Vish", "Bangalore", 23, 'asljlkj22', 'std1233')
# #
# # librarian = Librarian("Awantik", "Bangalore", 34, 'asljlkj22', 'zeke101')
# # print(m1)
# # print(librarian)

# b = catalog.searchByName('Shoe Dog')
# print(b)

# #print(catalog.searchByAuthor('J Foer'))

# #catalog.removeBookItem('Shoe Dog', '124hg')
# catalog.removeBookFromCatalog('Shoe Dog')
# print('\n')
# catalog.displayAllBooks()
# #m1.issueBook

# print('\n------------------\n')

librarian = Librarian("Awantik", "Bangalore", 34, 'asljlkj22', 'zeke101')

book1 = librarian.addBook('A novel', 'Ashish Kaul', 2020, 242)
book2 = librarian.addBook('Moonwalking with Einstien', 'J Foer', 2017, 318)
book3 = librarian.addBook('I heard you paint houses', 'Charles Brandt', 2004,
                          338)

librarian.addBookItem(book1, '101hg', 'H1A1')
librarian.addBookItem(book1, '102hg', 'H1A2')
librarian.addBookItem(book1, '103hg', 'H1A3')

librarian.addBookItem(book2, '201hg', 'H1B1')
librarian.addBookItem(book2, '202hg', 'H1B2')

librarian.addBookItem(book3, '301hg', 'H1C1')
librarian.addBookItem(book3, '302hg', 'H1C2')

librarian.displayAllBooks()

librarian.removeBookFromCatalog('A novel')

librarian.displayAllBooks()

member = Member("Ashish", "Bangalore", 23, 'asljlkj22', 'std1233')
