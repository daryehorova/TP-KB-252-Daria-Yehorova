import math
#Дискримінант
def diskr(a, b, c):
    D = b * b - 4 * a * c
    return D
# Знаходження коренів
def solve_equation(a, b, c):
    if a == 0:
        print("Коефіцієнт 'a' не може бути 0")
        return

    D = diskr(a, b, c)
    print("D =", D)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:
        print("Коренів немає (D < 0)")
# Введення даних
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))
# Виклик функції
solve_equation(a, b, c)