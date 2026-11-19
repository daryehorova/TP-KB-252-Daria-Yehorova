from stack import Stack
class RPNCalculator:
    PRIORITY = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
    }

    @staticmethod
    def tokenize(expression: str) -> list:
        tokens = []
        number_buffer = ""
        expression = expression.replace("−", "-")

        for char in expression:
            if char.isdigit() or char == ".":
                number_buffer += char
            else:
                if number_buffer:
                    tokens.append(number_buffer)
                    number_buffer = ""
                if char.isspace():
                    continue
                elif char in RPNCalculator.PRIORITY or char in ("(", ")"):
                    tokens.append(char)
                else:
                    raise ValueError(f"Unknown character in expression: '{char}'")

        if number_buffer:
            tokens.append(number_buffer)

        return tokens

    @staticmethod
    def _is_number(token: str) -> bool:
        try:
            float(token)
            return True
        except ValueError:
            return False

    def to_rpn(self, expression: str) -> list:
        tokens = self.tokenize(expression)
        output = []
        stack = Stack()

        for token in tokens:
            if self._is_number(token):
                output.append(token)
            elif token == "(":
                stack.push(token)
            elif token == ")":
                while not stack.is_empty() and stack.peek() != "(":
                    output.append(stack.pop())
                if stack.is_empty():
                    raise ValueError("Mismatched parentheses in expression")
                stack.pop()
            elif token in self.PRIORITY:
                while (
                    not stack.is_empty()
                    and stack.peek() in self.PRIORITY
                    and self.PRIORITY[stack.peek()] >= self.PRIORITY[token]
                ):
                    output.append(stack.pop())
                stack.push(token)

        while not stack.is_empty():
            top = stack.pop()
            if top == "(":
                raise ValueError("Mismatched parentheses in expression")
            output.append(top)

        return output

    def evaluate_rpn(self, rpn_tokens: list) -> float:
        stack = Stack()

        for token in rpn_tokens:
            if self._is_number(token):
                stack.push(float(token))
            elif token in self.PRIORITY:
                if len(stack) < 2:
                    raise ValueError("Invalid expression: not enough operands")
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.push(a + b)
                elif token == "-":
                    stack.push(a - b)
                elif token == "*":
                    stack.push(a * b)
                elif token == "/":
                    if b == 0:
                        raise ZeroDivisionError("Division by zero is not allowed")
                    stack.push(a / b)
                elif token == "^":
                    stack.push(a ** b)

        if len(stack) != 1:
            raise ValueError("Invalid expression after evaluation")
        return stack.pop()

    def calculate(self, expression: str) -> tuple[str, float]:
        rpn_tokens = self.to_rpn(expression)
        rpn_string = " ".join(rpn_tokens)
        result = self.evaluate_rpn(rpn_tokens)
        return rpn_string, result