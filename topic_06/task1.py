import logging
from functions import add, subtract, multiply, divide
from operations import get_number, get_operation

logging.basicConfig(
    filename='calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def calculator():
    print("Модульний калькулятор з логуванням")
    print("Для виходу введіть 'q' на будь-якому етапі.\n")
    logging.info("Програму калькулятор запущено.")
    
    while True:
        operation = get_operation()
        if operation == 'q':
            print("Вихід з програми. До побачення!")
            logging.info("Користувач завершив роботу програми.")
            break
            
        num1 = get_number("Введіть перше число: ")
        if num1 == 'q':
            logging.info("Користувач перервав введення на першому числі.")
            break   
        num2 = get_number("Введіть друге число: ")
        if num2 == 'q':
            logging.info("Користувач перервав введення на другому числі.")
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
            log_msg = f"Операція: {num1} {operation} {num2} = {result}"
            logging.info(log_msg)
            
        except ZeroDivisionError as ex:
            print(f"[Попередження] Помилка обчислення: {ex}\n")
            logging.warning(f"Помилка обчислення: {num1} {operation} {num2} -> {ex}")
        except Exception as ex:
            print(f"Сталася непередбачувана помилка: {ex}\n")
            logging.error(f"Непередбачувана помилка: {ex}")

if __name__ == "__main__":
    calculator()