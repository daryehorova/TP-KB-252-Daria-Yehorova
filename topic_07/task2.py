class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

def main():
    students = [
        Student("Олександр", 20),
        Student("Марія", 19),
        Student("Андрій", 22),
        Student("Софія", 18),
        Student("Дмитро", 21)
    ]

    print("Початковий список")
    for s in students:
        print(s)

    print("\nСортування за віком (за зростанням)")
    sorted_by_age = sorted(students, key=lambda s: s.age)
    for s in sorted_by_age:
        print(s)

    print("\nСортування за іменем (за алфавітом)")
    sorted_by_name = sorted(students, key=lambda s: s.name)
    for s in sorted_by_name:
        print(s)

if __name__ == "__main__":
    main()