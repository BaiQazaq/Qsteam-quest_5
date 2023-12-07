# 7. Create a function that checks if a string has balanced symbols using stacks and queues.

class Stack():
    def __init__(self):
        self.stack = []
        self.name = "Stack"

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

class Queue():
    def __init__(self):
        self.queue = []
        self.name = "Queue"

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)


def is_balanced(expression):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False

    return len(stack) == 0

def check_balance(iter, name):
    for expression in iter:
        if is_balanced(expression):
            print(f'The {name} expression "{expression}" is balanced.')
        else:
            print(f'The {name} expression "{expression}" is not balanced.')

# Example usage
if __name__ == "__main__":
    stack = Stack()
    queue = Queue()


    stack.push("((a + b) * (c - d))")
    queue.enqueue("{[a + b] * (c - d)}")
    stack.push("((a + b) * (c - d}")
    queue.enqueue("[(a + b) * (c - d)]")

    print(stack.stack)
    print(queue.queue)

    check_balance(stack.stack, stack.name)
    check_balance(queue.queue, queue.name)