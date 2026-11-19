from student import Student
from student_list import StudentList
from utils import Utils

def test_find_position():
    s_list = StudentList()
    s_list.add_student(Student("Bob", "0631234567", "bob@gmail.com", "19"))
    s_list.add_student(Student("Emma", "0631234567", "emma@gmail.com", "20"))
    s_list.add_student(Student("Jon", "0631234567", "jon@gmail.com", "18"))
    s_list.add_student(Student("Zak", "0631234567", "zak@gmail.com", "21"))

    assert s_list.find_position("Bob") == 0
    assert s_list.find_position("Emma") == 1
    assert s_list.find_position("Zak") == 3
    assert s_list.find_position("Michael") == 3

def test_add_student():
    s_list = StudentList()
    s_list.add_student(Student("Emma", "0631234567", "emma@gmail.com", "20"))
    s_list.add_student(Student("Anna", "12121212", "anna@gmail.com", "18"))
    assert s_list.students[0].name == "Anna"

    s_list.add_student(Student("Bob", "12121212", "bob@gmail.com", "19"))
    assert s_list.students[1].name == "Bob"

    s_list.add_student(Student("Zak", "12121212", "zak@gmail.com", "22"))
    assert s_list.students[3].name == "Zak"

def test_delete_student():
    s_list = StudentList()
    s_list.add_student(Student("Bob", "0631234567", "bob@gmail.com", "19"))
    s_list.add_student(Student("Emma", "0631234567", "emma@gmail.com", "20"))

    assert s_list.students[0].name == "Bob"
    assert s_list.delete_student("Bob") is True
    assert s_list.students[0].name == "Emma"
    assert s_list.delete_student("NonExistent") is False

def test_update_student():
    s_list = StudentList()
    s_list.add_student(Student("Bob", "0631234567", "bob@gmail.com", "19"))
    s_list.add_student(Student("Zak", "0631234567", "zak@gmail.com", "21"))

    assert s_list.update_student("Bob", new_name="Aaron", new_age="20") is True
    assert s_list.students[0].name == "Aaron"
    assert s_list.students[0].age == "20"
    assert s_list.students[0].phone == "0631234567"

def test_save_load(tmp_path):
    s_list = StudentList()
    s_list.add_student(Student("Charlie", "555", "ch@mail.com", "20"))

    file_name = tmp_path / "test_students.csv"
    Utils.save_to_file(str(file_name), s_list)

    loaded_list = StudentList()
    Utils.load_from_file(str(file_name), loaded_list)

    assert len(loaded_list.students) == 1
    assert loaded_list.students[0].name == "Charlie"
    assert loaded_list.students[0].phone == "555"