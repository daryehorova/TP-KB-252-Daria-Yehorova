from functions import add, subtract, multiply, divide
from operations import get_number, get_operation

def calculator():
    print("Модульний калькулятор")
    print("Для виходу введіть 'q' на будь-якому етапі.\n")
    
    while True:
        operation = get_operation()
        if operation == 'q':
            print("Вихід з програми. До побачення!")
            break
            
        num1 = get_number("Введіть перше число: ")
        if num1 == 'q':
            break   
        num2 = get_number("Введіть друге число: ")
        if num2 == 'q':
            break
            
        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
                
            print(f"Результат: {result}\n")
            
        except ZeroDivisionError as ex:
            print(f"[Попередження] Помилка обчислення: {ex}\n")
        except Exception as ex:
            print(f"Сталася непередбачувана помилка: {ex}\n")

if __name__ == "__main__":
    calculator()