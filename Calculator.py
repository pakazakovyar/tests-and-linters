
class Calculator:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def infix_to_postfix(self, expression):
        stack = []
        postfix = []
        i = 0
        n = len(expression)

        while i < n:
            char = expression[i]

            if char == ' ':
                i += 1
                continue

            if char.isdigit():
                num = []
                while i < n and (expression[i].isdigit() or expression[i] == '.'):
                    num.append(expression[i])
                    i += 1
                postfix.append(''.join(num))
                continue

            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1] != '(' and
                       self.precedence.get(stack[-1], 0) >= self.precedence.get(char, 0)):
                    postfix.append(stack.pop())
                stack.append(char)

            i += 1

        while stack:
            postfix.append(stack.pop())

        return ' '.join(postfix)

    def evaluate_postfix(self, postfix_expression):
        stack = []
        tokens = postfix_expression.split()

        for token in tokens:
            if token.replace('.', '').isdigit():
                stack.append(float(token))
            else:
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(left / right)

        return stack[0]

    def calculate(self, expression):
        try:
            postfix = self.infix_to_postfix(expression)
            result = self.evaluate_postfix(postfix)
            return result
        except Exception as e:
            return f"Ошибка: {str(e)}"


if __name__ == "__main__":
    calc = Calculator()
    while True:
        print("\nВведите арифметическое выражение (или 'exit' для выхода):")
        user_input = input().strip()

        if user_input.lower() == 'exit':
            break

        if not user_input:
            continue

        result = calc.calculate(user_input)
        print(f"Результат: {result}")