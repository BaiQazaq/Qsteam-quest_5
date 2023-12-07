# 1. Implement a stack using arrays.
# 2. Write a program to push an element onto a stack.
# 3. Create a function to pop an element from a stack.
# 4. Implement a method to check if a stack is empty.
# 5. Write a function that returns the top element of a stack.


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
