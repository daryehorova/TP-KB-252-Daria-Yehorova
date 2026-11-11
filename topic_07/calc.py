import logging
from functions import MathOperations
from operations import InputHandler

logging.basicConfig(
    filename='calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class Calculator:
    def __init__(self):
        logging.info("ООП Калькулятор запущено.")

    def run(self):
        print("ООП Модульний калькулятор з логуванням")
        print("Для виходу введіть 'q' на будь-якому етапі.\n")
        
        while True:
            operation = InputHandler.get_operation()
            if operation == 'q':
                print("Вихід з програми. До побачення!")
                logging.info("Користувач завершив роботу програми.")
                break
                
            num1 = InputHandler.get_number("Введіть перше число: ")
            if num1 == 'q':
                break   
            num2 = InputHandler.get_number("Введіть друге число: ")
            if num2 == 'q':
                break
                
            try:
                if operation == '+':
                    result = MathOperations.add(num1, num2)
                elif operation == '-':
                    result = MathOperations.subtract(num1, num2)
                elif operation == '*':
                    result = MathOperations.multiply(num1, num2)
                elif operation == '/':
                    result = MathOperations.divide(num1, num2)
                    
                print(f"Результат: {result}\n")
                logging.info(f"Операція: {num1} {operation} {num2} = {result}")
                
            except ZeroDivisionError as ex:
                print(f"[Попередження] Помилка обчислення: {ex}\n")
                logging.warning(f"Помилка обчислення: {num1} {operation} {num2} -> {ex}")
            except Exception as ex:
                print(f"Сталася непередбачувана помилка: {ex}\n")
                logging.error(f"Непередбачувана помилка: {ex}")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()