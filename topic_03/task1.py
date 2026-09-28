def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y == 0:
        return "Помилка: ділення на нуль"
    return x / y

while True:
    print("\n Калькулятор ")
    print("Введіть 'exit' або 'off' для виходу з програми")
    
    op = input("Введіть операцію (+, -, *, /): ")
    if op.lower() == 'exit' or op.lower() == 'off':
        print("Роботу калькулятора завершено")
        break

    if op not in ['+', '-', '*', '/']:
        print("Невідома операція")
        continue

    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b)
    elif op == '*':
        res = mul(a, b)
    elif op == '/':
        res = div(a, b)
    print("Результат:", res)