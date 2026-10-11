
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@gmail.com", "age":"19"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "age":"20"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@gmail.com", "age":"18"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@gmail.com", "age":"21"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Email is " + elem["email"] + ", Age is " + elem["age"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    age = input("Please enter student age: ")
    newItem = {"name": name, "phone": phone, "email": email, "age": age}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    foundItem = None
    for item in list:
        if name == item["name"]:
            foundItem = item
            break
            
    if foundItem is None:
        print("Element was not found")
    else:
        print("Current data -> Name: " + foundItem["name"] + ", Phone: " + foundItem["phone"] + ", Email: " + foundItem["email"] + ", Age: " + foundItem["age"])
        print("Enter new data (leave blank to keep existing value):")
        
        new_name = input("New name [" + foundItem["name"] + "]: ").strip()
        new_phone = input("New phone [" + foundItem["phone"] + "]: ").strip()
        new_email = input("New email [" + foundItem["email"] + "]: ").strip()
        new_age = input("New age [" + foundItem["age"] + "]: ").strip()

        list.remove(foundItem)
        
        if new_name:
            foundItem["name"] = new_name
        if new_phone:
            foundItem["phone"] = new_phone
        if new_email:
            foundItem["email"] = new_email
        if new_age:
            foundItem["age"] = new_age

        insertPosition = 0
        for item in list:
            if foundItem["name"] > item["name"]:
                insertPosition += 1
            else:
                break
        list.insert(insertPosition, foundItem)
        print("Element has been updated")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()