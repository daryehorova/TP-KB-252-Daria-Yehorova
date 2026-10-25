def get_number(prompt: str):
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() == 'q':
                return 'q'
            return float(user_input)
        except ValueError:
            print("Помилка: Введено нечислове значення. Спробуйте ще раз.")

def get_operation():
    while True:
        operation = input("Введіть операцію (+, -, *, /): ").strip()
        if operation.lower() == 'q':
            return 'q'
        if operation in ('+', '-', '*', '/'):
            return operation
        print("Помилка: Невідома операція. Використовуйте +, -, *, /.")