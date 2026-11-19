from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def find_position(self, name):
        position = 0
        for student in self.students:
            if student.name < name:
                position += 1
            else:
                break
        return position

    def add_student(self, student: Student):
        insert_position = self.find_position(student.name)
        self.students.insert(insert_position, student)
        print("New element has been added")
        return True

    def delete_student(self, name):
        position = self.find_position(name)
        if position < len(self.students) and self.students[position].name == name:
            del self.students[position]
            print("Element has been deleted")
            return True
        else:
            print("Element was not found")
            return False

    def update_student(self, name, new_name="", new_phone="", new_email="", new_age=""):
        position = self.find_position(name)
        if position < len(self.students) and self.students[position].name == name:
            student = self.students.pop(position)
            
            if new_name:
                student.name = new_name
            if new_phone:
                student.phone = new_phone
            if new_email:
                student.email = new_email
            if new_age:
                student.age = new_age

            self.add_student(student)
            print("Element has been updated")
            return True
        else:
            print("Element was not found")
            return False

    def get_student(self, name):
        position = self.find_position(name)
        if position < len(self.students) and self.students[position].name == name:
            return self.students[position]
        return None

    def print_all(self):
        for student in self.students:
            print(student)