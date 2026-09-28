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

a = float(input("Введіть перше число: "))
op = input("Введіть операцію (+, -, *, /): ")
b = float(input("Введіть друге число: "))

match op:
    case "+":
        res = add(a, b)
    case "-":
        res = sub(a, b)
    case "*":
        res = mul(a, b)
    case "/":
        res = div(a, b)
    case _:
        res = "Невірний знак"

print("Результат:", res)