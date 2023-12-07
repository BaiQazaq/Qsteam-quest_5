from collections import deque

def generate_binary_numbers(n):
    if n <= 0:
        return []

    result = []
    queue = deque(["1"])

    for _ in range(n):
        binary_number = queue.popleft()
        result.append(binary_number)

        # Enqueue the next binary numbers by appending '0' and '1' to the current binary number
        queue.append(binary_number + '0')
        queue.append(binary_number + '1')

    return result

# Example usage
if __name__ == "__main__":
    n = 20
    binary_numbers = generate_binary_numbers(n)

    print(f"{n} Binary Numbers:")
    for binary_number in binary_numbers:
        print(binary_number)
