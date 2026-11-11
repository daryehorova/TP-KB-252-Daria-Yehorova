def demonstrate_sorting():
    students = [
        {"name": "Олександр", "grade": 85},
        {"name": "Марія", "grade": 92},
        {"name": "Андрій", "grade": 74},
        {"name": "Софія", "grade": 95},
        {"name": "Дмитро", "grade": 68}
    ]

    print("Початковий список студентів")
    for s in students:
        print(f"Ім'я: {s['name']}, Оцінка: {s['grade']}")
        
    sorted_by_grade = sorted(students, key=lambda x: x["grade"])
    print("\nСортування за оцінкою (за зростанням)")
    for s in sorted_by_grade:
        print(f"Ім'я: {s['name']}, Оцінка: {s['grade']}")
        
    sorted_by_grade_desc = sorted(students, key=lambda x: x["grade"], reverse=True)
    print("\nСортування за оцінкою (за спаданням)")
    for s in sorted_by_grade_desc:
        print(f"Ім'я: {s['name']}, Оцінка: {s['grade']}")
        
    sorted_by_name = sorted(students, key=lambda x: x["name"])
    print("\nСортування за ім'ям (за алфавітом)")
    for s in sorted_by_name:
        print(f"Ім'я: {s['name']}, Оцінка: {s['grade']}")

if __name__ == "__main__":
    demonstrate_sorting()