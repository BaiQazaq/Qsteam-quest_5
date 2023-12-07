# 7. Implement a stack that supports retrieving the minimum element in constant time.


class MinStack:
    def __init__(self):
        self.stack = []  # Main stack
        self.min_stack = []  # Auxiliary stack for minimum elements

    def push(self, value):
        self.stack.append(value)

        # Update the minimum stack
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        popped_value = self.stack.pop()

        # Update the minimum stack
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()

        return popped_value

    def get_min(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]

# Example usage
if __name__ == "__main__":
    min_stack = MinStack()

    min_stack.push(3)
    min_stack.push(5)
    print("Minimum element:", min_stack.get_min())  # Output: 3

    min_stack.push(2)
    min_stack.push(1)
    print("Minimum element:", min_stack.get_min())  # Output: 1

    min_stack.pop()
    print("Minimum element:", min_stack.get_min())  # Output: 2
