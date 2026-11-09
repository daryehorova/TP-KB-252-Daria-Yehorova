import csv
import lab_02

def test_findPosition():
    listForFind = [
        {"name":"Bob", "phone":"0631234567", "email":"bob@gmail.com", "age":"19"},
        {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "age":"20"},
        {"name":"Jon",  "phone":"0631234567", "email":"jon@gmail.com", "age":"18"},
        {"name":"Zak",  "phone":"0631234567", "email":"zak@gmail.com", "age":"21"}
    ]
    
    assert lab_02.findPosition(listForFind, "Bob") == 0    
    assert lab_02.findPosition(listForFind, "Emma") == 1
    assert lab_02.findPosition(listForFind, "Zak") == 3
    assert lab_02.findPosition(listForFind, "Michael") == 3

def test_addNewElement():
    listForAdd = [
        {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "age":"20"},
    ]
    
    lab_02.addNewElement(listForAdd, {"name": "Anna", "phone": "12121212", "email": "anna@gmail.com", "age": "18"})
    assert listForAdd[0]["name"] == "Anna"

    lab_02.addNewElement(listForAdd, {"name": "Bob", "phone": "12121212", "email": "bob@gmail.com", "age": "19"})
    assert listForAdd[1]["name"] == "Bob"

    lab_02.addNewElement(listForAdd, {"name": "Zak", "phone": "12121212", "email": "zak@gmail.com", "age": "22"})
    assert listForAdd[3]["name"] == "Zak"

def test_deleteElement():
    listForDel = [
        {"name":"Bob", "phone":"0631234567", "email":"bob@gmail.com", "age":"19"},
        {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "age":"20"},
        {"name":"Jon",  "phone":"0631234567", "email":"jon@gmail.com", "age":"18"},
        {"name":"Zak",  "phone":"0631234567", "email":"zak@gmail.com", "age":"21"}
    ]

    assert listForDel[0]["name"] == "Bob"
    assert lab_02.deleteElement(listForDel, "Bob") == True
    assert listForDel[0]["name"] == "Emma"

def test_save_load(tmp_path):
    test_list = []
    lab_02.addNewElement(test_list, {"name": "Charlie", "phone": "555", "email": "ch@mail.com", "age": "20"})

    fileName = tmp_path / "test_students.csv"
    
    lab_02.saveToFile(str(fileName), test_list)
    
    loaded_list = []
    lab_02.loadFromFile(str(fileName), loaded_list)

    assert len(loaded_list) == 1
    assert loaded_list[0]["name"] == "Charlie"