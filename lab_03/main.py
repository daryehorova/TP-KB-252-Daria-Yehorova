from sys import argv
from student import Student
from student_list import StudentList
from utils import Utils

def main():
    if len(argv) > 1:
        filename = argv[1]
    else:
        filename = "lab3.csv"

    group_list = StudentList()
    Utils.load_from_file(filename, group_list)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                email = input("Please enter student email: ")
                age = input("Please enter student age: ")
                new_student = Student(name, phone, email, age)
                group_list.add_student(new_student)

            case "U" | "u":
                print("Existing element will be updated")
                name = input("Please enter name to be updated: ")
                found_student = group_list.get_student(name)
                if found_student:
                    print(f"Current data -> Name: {found_student.name}, Phone: {found_student.phone}, Email: {found_student.email}, Age: {found_student.age}")
                    print("Enter new data (leave blank to keep existing value):")
                    new_name = input(f"New name [{found_student.name}]: ").strip()
                    new_phone = input(f"New phone [{found_student.phone}]: ").strip()
                    new_email = input(f"New email [{found_student.email}]: ").strip()
                    new_age = input(f"New age [{found_student.age}]: ").strip()
                    group_list.update_student(name, new_name, new_phone, new_email, new_age)
                else:
                    print("Element was not found")

            case "D" | "d":
                print("Element will be deleted")
                name = input("Please enter name to be deleted: ")
                group_list.delete_student(name)

            case "P" | "p":
                print("List will be printed")
                group_list.print_all()

            case "X" | "x":
                print("Exit()")
                Utils.save_to_file(filename, group_list)
                break

            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()