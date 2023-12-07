# 3. Create a program to convert infix expressions to postfix using stacks.


class InfixToPostfix:
    def __init__(self):
        self.operator_stack = []
        self.output = []

    def is_operator(self, char):
        return char in {'+', '-', '*', '/'}

    def get_precedence(self, operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        else:
            return 0

    def infix_to_postfix(self, infix_expression):
        for char in infix_expression:
            if char.isalnum():
                # Operand, append to output
                self.output.append(char)
            elif char == '(':
                # Left parenthesis, push to operator stack
                self.operator_stack.append(char)
            elif char == ')':
                # Right parenthesis, pop operators from stack to output until a matching '(' is found
                while self.operator_stack and self.operator_stack[-1] != '(':
                    self.output.append(self.operator_stack.pop())
                self.operator_stack.pop()  # Pop the '('
            elif self.is_operator(char):
                # Operator, pop operators from stack to output until stack is empty or top has lower precedence
                while self.operator_stack and self.get_precedence(self.operator_stack[-1]) >= self.get_precedence(char):
                    self.output.append(self.operator_stack.pop())
                self.operator_stack.append(char)

        # Pop any remaining operators from stack to output
        while self.operator_stack:
            self.output.append(self.operator_stack.pop())

        # Convert the list to a string and return
        return ''.join(self.output)

# Example usage
if __name__ == "__main__":
    infix_expression = "a + b * (c - d) / e"
    converter = InfixToPostfix()
    postfix_expression = converter.infix_to_postfix(infix_expression)

    print("Infix Expression:", infix_expression)
    print("Postfix Expression:", postfix_expression)
