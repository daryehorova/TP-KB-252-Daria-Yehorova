import csv
from sys import argv

globalList = []

def printAllList(listForPrint):
    for elem in listForPrint:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Email is " + elem["email"] + ", Age is " + elem["age"]
        print(strForPrint)
    return

def findPosition(listForFind, name):
    position = 0
    for item in listForFind:
        if item["name"] < name:
            position += 1
        else:
            break
    return position

def addNewElement(listForAdd, newItem):
    insertPosition = findPosition(listForAdd, newItem["name"])
    listForAdd.insert(insertPosition, newItem)
    print("New element has been added")
    return True

def deleteElement(listForDel, name):
    position = findPosition(listForDel, name)
    if position < len(listForDel) and listForDel[position]["name"] == name:
        del listForDel[position]
        print("Element has been deleted")
        return True
    else:
        print("Element was not found")
        return False

def updateElement(listForUpdate):
    name = input("Please enter name to be updated: ")
    position = findPosition(listForUpdate, name)
    
    if position < len(listForUpdate) and listForUpdate[position]["name"] == name:
        foundItem = listForUpdate[position]
        print(f"Current data -> Name: {foundItem['name']}, Phone: {foundItem['phone']}, Email: {foundItem['email']}, Age: {foundItem['age']}")
        print("Enter new data (leave blank to keep existing value):")
        
        new_name = input(f"New name [{foundItem['name']}]: ").strip()
        new_phone = input(f"New phone [{foundItem['phone']}]: ").strip()
        new_email = input(f"New email [{foundItem['email']}]: ").strip()
        new_age = input(f"New age [{foundItem['age']}]: ").strip()

        listForUpdate.pop(position)
        
        if new_name:
            foundItem["name"] = new_name
        if new_phone:
            foundItem["phone"] = new_phone
        if new_email:
            foundItem["email"] = new_email
        if new_age:
            foundItem["age"] = new_age

        addNewElement(listForUpdate, foundItem)
        print("Element has been updated")
        return True
    else:
        print("Element was not found")
        return False

def loadFromFile(filename, listToLoad):
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row.get("Name") or row.get("name")
                phone = row.get("Phone") or row.get("phone")
                email = row.get("Email") or row.get("email")
                age = row.get("Age") or row.get("age")
                
                if name and phone:
                    newItem = {
                        "name": name, 
                        "phone": phone, 
                        "email": email if email else "", 
                        "age": age if age else ""
                    }
                    addNewElement(listToLoad, newItem)
        print(f"Data successfully loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    except Exception as e:
        print(f"An error occurred while loading: {e}")

def saveToFile(filename, listToSave):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "email", "age"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in listToSave:
                writer.writerow(item)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def main():
    if len(argv) > 1:
        filename = argv[1]
    else:
        filename = "lab2.csv"
        
    loadFromFile(filename, globalList)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                email = input("Please enter student email: ")
                age = input("Please enter student age: ")
                newItem = {"name": name, "phone": phone, "email": email, "age": age}
                addNewElement(globalList, newItem)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(globalList)
            case "D" | "d":
                print("Element will be deleted")
                name = input("Please enter name to be deleted: ")
                deleteElement(globalList, name)
            case "P" | "p":
                print("List will be printed")
                printAllList(globalList)
            case "X" | "x":
                print("Exit()")
                saveToFile(filename, globalList)
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()