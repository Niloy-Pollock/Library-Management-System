class Student:
    def __init__(self, name, email, phone, address, password) -> None:
        self.name = name 
        self.email = email
        self.phone = phone
        self.address = address
        self.password = password

    def __str__(self) -> str:
        return self.name



class Book:
    def __init__(self, name, writer, publisher, available, language, genre) -> None:
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.available = available
        self.language =  language
        self.genre = genre

    def __str__(self) -> str:
        return f"name = {self.name}, writer = {self.writer}"



book_name = []
book_list = []

admin = Student("farhan", "farhan@gmail.com", "0123459392", "Mirpur, dhaka", "1234")
student_list = [admin]


def add_student(student):
    student_list.append(student)

def add_book(book):
    book_list.append(book)
    book_name.append(book.name)

def Authenticate(username, password):
    for el in student_list:
        if el.name == username:
            if el.password == password:
                return True
            else:
                return False

