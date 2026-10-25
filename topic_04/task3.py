def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    raise ZeroDivisionError("Ділення на нуль неможливе.")
  return a / b

def get_number(prompt: str):
  while True:
    try:
      user_input = input(prompt)
      if user_input.lower() == "q":
        return "q"
      return float(user_input)
    except ValueError:
      print("Помилка: Будь ласка, введіть коректне числове значення.")

def get_operation():
  while True:
    operation = input("Введіть операцію (+, -, *, /): ").strip()
    if operation.lower() == "q":
      return "q"
    if operation in ("+", "-", "*", "/"):
      return operation
    print("Помилка: невідома операція.")

def calculator_task3():
  print("Калькулятор")
  print("Для виходу введіть 'q' на будь-якому етапі.\n")

  while True:
    operation = get_operation()
    if operation == "q":
      print("Вихід з програми. До побачення!")
      break
    num1 = get_number("Введіть перше число: ")
    if num1 == "q":
      break
    num2 = get_number("Введіть друге число: ")
    if num2 == "q":
      break

    try:
      if operation == "+":
        result = add(num1, num2)
      elif operation == "-":
        result = subtract(num1, num2)
      elif operation == "*":
        result = multiply(num1, num2)
      elif operation == "/":
        result = divide(num1, num2)

      print(f"Результат: {result}\n")

    except ZeroDivisionError as ex:
      print("[Попередження] Виникла математична помилка:")
      print(f"Тип помилки: {type(ex)}")
      print(f"Аргументи помилки: {ex.args}")
      print(f"Опис: {ex}\n")

    except ArithmeticError as ex:
      print(f"Арифметична помилка: {ex}\n")

    except Exception as ex:
      print(f"Сталася непередбачувана помилка: {ex}\n")
      print(f"Тип: {type(ex)}, Аргументи: {ex.args}\n")

if __name__ == "__main__":
  calculator_task3()