import csv
from student import Student
from student_list import StudentList

class Utils:
    @staticmethod
    def load_from_file(filename, student_list: StudentList):
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row.get("Name") or row.get("name")
                    phone = row.get("Phone") or row.get("phone")
                    email = row.get("Email") or row.get("email")
                    age = row.get("Age") or row.get("age")

                    if name and phone:
                        student = Student(
                            name=name,
                            phone=phone,
                            email=email if email else "",
                            age=age if age else ""
                        )
                        student_list.add_student(student)
            print(f"Data successfully loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty list.")
        except Exception as e:
            print(f"An error occurred while loading: {e}")

    @staticmethod
    def save_to_file(filename, student_list: StudentList):
        try:
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                fieldnames = ["name", "phone", "email", "age"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list.students:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "email": student.email,
                        "age": student.age
                    })
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving: {e}")