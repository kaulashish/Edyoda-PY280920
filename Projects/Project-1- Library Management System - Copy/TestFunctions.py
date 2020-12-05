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

member1 = Member('Ashish', 'Himachal Pradesh', '23', '18002822833', 'abc111')

librarian.removeBookItemFromCatalog('A novel', '101hg')
librarian.displayAllBooks()