"""Модуль для вычисления математических
выражений в инфиксной и постфиксной форме."""


class Calculator:
    """Калькулятор, преобразующий инфиксные
     выражения в постфиксные и вычисляющий их."""

    def __init__(self):
        """Инициализация приоритетов операторов."""
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def infix_to_postfix(self, expression):
        """Преобразует инфиксное выражение в
        постфиксное (обратную польскую запись)."""
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
                while i < n and (expression[i].isdigit() or
                                 expression[i] == '.'):
                    num.append(expression[i])
                    i += 1
                postfix.append(''.join(num))
                continue

            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if not stack:
                    raise ValueError("Несогласованные скобки")
                stack.pop()
            else:
                if char not in self.precedence:
                    raise ValueError(f"Неизвестный оператор: {char}")
                while (stack and stack[-1] != '(' and
                       self.precedence.get(stack[-1], 0)
                       >= self.precedence.get(char, 0)):
                    postfix.append(stack.pop())
                stack.append(char)

            i += 1

        while stack:
            if stack[-1] == '(':
                raise ValueError("Несогласованные скобки")
            postfix.append(stack.pop())

        return ' '.join(postfix)

    def evaluate_postfix(self, postfix_expression):
        """Вычисляет значение выражения в постфиксной форме."""
        stack = []
        tokens = postfix_expression.split()

        for token in tokens:
            if token.replace('.', '').isdigit():
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов для оператора")
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    if right == 0:
                        raise ZeroDivisionError("Деление на ноль")
                    stack.append(left / right)
                else:
                    raise ValueError(f"Неизвестный оператор: {token}")

        if len(stack) != 1:
            raise ValueError("Некорректное выражение")

        return stack[0]

    def calculate(self, expression):
        """Вычисляет результат инфиксного выражения."""
        postfix = self.infix_to_postfix(expression)
        result = self.evaluate_postfix(postfix)
        return result
