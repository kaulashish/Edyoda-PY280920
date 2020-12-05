from Catalog import Catalog


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id


class Member(User):
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    def displayAllBooks(self):
        pass

    #assume name is unique
    def issueBook(self, name, days=10):
        pass

    #assume name is unique
    def returnBook(self, name):
        pass


class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        Catalog.__init__(self)
        self.emp_id = emp_id

    def __repr__(self):
        return self.name + self.location + self.emp_id

    def addBook(self, name, author, publish_date, pages):
        return Catalog.addBook(self, name, author, publish_date, pages)

    def addBookItem(self, book, isbn, rack):
        Catalog.addBookItem(self, book, isbn, rack)

    def searchByName(self, name):
        return Catalog.searchByName(self, name)

    def searchByAuthor(self, author):
        return Catalog.searchByAuthor(self, author)

    def removeBook(self, name):
        Catalog.removeBookFromCatalog(self, name)

    def removeBookItemFromCatalog(self, book, isbn):
        Catalog.removeBookItem(self, book, isbn)

    def displayAllBooks(self):
        Catalog.displayAllBooks(self)

    def lendbook(self, name):
        pass
