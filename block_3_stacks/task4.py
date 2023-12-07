# 8. Write a method to reverse a stack using recursion.

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

def sort_stack(stack):
    if not stack.is_empty():
        # Pop the top element
        top_element = stack.pop()

        # Recursively sort the remaining stack
        sort_stack(stack)

        # Insert the top element in sorted order
        insert_sorted(stack, top_element)

def insert_sorted(stack, item):
    if stack.is_empty() or item > stack.peek():
        stack.push(item)
    else:
        # Pop elements greater than the current item
        top_element = stack.pop()

        # Recursively insert the current item in sorted order
        insert_sorted(stack, item)

        # Push the popped element back
        stack.push(top_element)

# Example usage
if __name__ == "__main__":
    my_stack = Stack()

    # Push elements onto the stack
    my_stack.push(4)
    my_stack.push(2)
    my_stack.push(7)
    my_stack.push(1)
    my_stack.push(5)

    print("Original Stack:", my_stack.items)

    # Sort the stack
    sort_stack(my_stack)

    print("Sorted Stack:", my_stack.items)
