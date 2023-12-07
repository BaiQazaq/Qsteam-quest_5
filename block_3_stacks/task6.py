# 10. Implement a stack-based algorithm to check for balanced parentheses in an expression.


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

# Example usage
if __name__ == "__main__":
    test_cases = [
        "((a + b) * (c - d))",
        "{[a + b] * (c - d)}",
        "((a + b) * (c - d}",
        "[(a + b) * (c - d)]",
    ]

    for expression in test_cases:
        if is_balanced(expression):
            print(f'The expression "{expression}" is balanced.')
        else:
            print(f'The expression "{expression}" is not balanced.')
