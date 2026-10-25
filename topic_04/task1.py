def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def get_number(prompt):
  "Функція для запиту даних від користувача з обробкою виняткових ситуацій (ValueError)."
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Помилка: Будь ласка, введіть коректне числове значення.")

def calculator_task1():
  print("Калькулятор")
  print("Для виходу введіть 'q'")

  while True:
    operation = input("Введіть операцію (+, -, *, /): ").strip()
    if operation.lower() == "q":
      break

    if operation not in ("+", "-", "*", "/"):
      print("Помилка: Невідома операція.")
      continue

    num1 = get_number("Введіть перше число: ")
    num2 = get_number("Введіть друге число: ")
    if operation == "+":
      result = add(num1, num2)
    elif operation == "-":
      result = subtract(num1, num2)
    elif operation == "*":
      result = multiply(num1, num2)
    elif operation == "/":
      result = divide(num1, num2)

    print(f"Результат: {result}\n")

if __name__ == "__main__":
  calculator_task1()