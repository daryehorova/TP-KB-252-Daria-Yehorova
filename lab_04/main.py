from sys import argv
from rpn import RPNCalculator

def process_expression(calculator: RPNCalculator, expression: str):
    try:
        rpn_str, result = calculator.calculate(expression)
        print(f"Expression: {expression}")
        print(f"RPN: {rpn_str}")
        print(f"Result: {result}\n")
    except Exception as e:
        print(f"Error processing '{expression}': {e}\n")

def main():
    calculator = RPNCalculator()

    if len(argv) > 1:
        filename = argv[1]
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                for line in file:
                    expr = line.strip()
                    if expr:
                        process_expression(calculator, expr)
        except FileNotFoundError:
            print(f"File {filename} not found. Switching to interactive mode.\n")
        except Exception as e:
            print(f"An error occurred while reading file: {e}\n")
    while True:
        choice = input("Please specify the action [ E evaluate expression, X exit ] ").strip()
        match choice:
            case "E" | "e":
                expression = input("Please enter mathematical expression: ").strip()
                if expression:
                    process_expression(calculator, expression)
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()