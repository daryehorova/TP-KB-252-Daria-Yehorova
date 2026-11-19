class Student:
    def __init__(self, name, phone, email="", age=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age

    def __str__(self):
        return f"Student name is {self.name},  Phone is {self.phone}, Email is {self.email}, Age is {self.age}"