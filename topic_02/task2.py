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

if op == "+":
    res = add(a, b)
elif op == "-":
    res = sub(a, b)
elif op == "*":
    res = mul(a, b)
elif op == "/":
    res = div(a, b)
else:
    res = "Невірний знак"

print("Результат:", res)