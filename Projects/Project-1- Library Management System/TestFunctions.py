# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

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

# librarian.removeBookFromCatalog('A novel')
# librarian.removeBookItem('A novel', '102hg')

librarian.displayAllBooks()

member1 = Member("Ashish", "Bangalore", 23, 'asljlkj22', 'std1233')

# print(member1.searchByAuthor('J Foer'))
# member1.displayAllBooks()

member1.issueBook('A novel')
member1.issueBook('Moonwalking with Einstien')
# member1.issueBook('Moonwalking with Einstien')
member1.issueBook('I heard you paint houses')

librarian.displayAllBooks()

member2 = Member('Abhinov', "Dharamshala", 19, '231514514', 'std232')
member2.issueBook('A novel')
member2.issueBook('Moonwalking with Einstien')

member3 = Member('Sunita', "Kangra", 27, '8722246464', 'std242')
member3.issueBook('A novel')
member3.issueBook('I heard you paint houses')

librarian.displayAllBooks()

member4 = Member('Kapil', "Dari", 33, '44454464', 'std112')
member4.issueBook('Moonwalking with Einstien')

librarian.displaylendedbooks()

member1.displayissuedbooks()

member1.returnBook('A novel')
member4.returnBook('A novel')
member2.returnBook('A novel')
member3.returnBook('A novel')
member1.returnBook('Moonwalking with Einstien')
member2.returnBook('Moonwalking with Einstien')
member1.returnBook('I heard you paint houses')
member3.returnBook('I heard you paint houses')

member1.displayAllBooks()

librarian.displaylendedbooks()

member3.displayissuedbooks()

# print(librarian.lended_book_data)
