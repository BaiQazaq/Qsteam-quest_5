# 6. Create a program to evaluate a postfix expression using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

    def evaluate_postfix(self, expression):
        stack = Stack()
        operators = set(['+', '-', '*', '/'])

        for symbol in expression:
            if symbol.isdigit():
                stack.push(int(symbol))
            elif symbol in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if symbol == '+':
                    result = operand1 + operand2
                elif symbol == '-':
                    result = operand1 - operand2
                elif symbol == '*':
                    result = operand1 * operand2
                elif symbol == '/':
                    result = operand1 / operand2

                stack.push(result)
        
        return stack.pop()



# Example usage
if __name__ == "__main__":
    stack = Stack()

    print("Is the stack empty? ", stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size: ", stack.size())
    print("Top element: ", stack.peek())

    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    print("Stack size after pop: ", stack.size())

    postfix_expression = "23*5+"
    result = stack.evaluate_postfix(postfix_expression)
    print(result)
