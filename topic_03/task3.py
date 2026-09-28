student = {
    "name": "Daria",
    "age": 18,
    "group": "KB-252"
}
print("Початковий словник:", student)

print("Ключі (keys):", list(student.keys()))

print("Значення (values):", list(student.values()))

print("Пари (items):", list(student.items()))

student.update({"age": 19, "city": "Chernigiv"})
print("Після update():", student)

del student["city"]
print("Після del['city']:", student)

student.clear()
print("Після clear():", student)