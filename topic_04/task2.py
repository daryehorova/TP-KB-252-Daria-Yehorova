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

def calculator_task2():
  print("Калькулятор")
  print("Для виходу введіть 'q'")

  while True:
    operation = input("Введіть операцію (+, -, *, /): ").strip()
    if operation.lower() == "q":
      break

    if operation not in ("+", "-", "*", "/"):
      print("Помилка: Невідома операція.")
      continue

    try:
      num1 = float(input("Введіть перше число: "))
      num2 = float(input("Введіть друге число: "))

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
    except ValueError as ex:
      print(f"Помилка введення даних (не число): {ex}\n")
    except Exception as ex:
      print(f"Сталася непередбачувана помилка: {ex}\n")

if __name__ == "__main__":
  calculator_task2()