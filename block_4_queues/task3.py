# 7. Implement a priority queue using a list.
# 8. Write a method to reverse the first K elements of a queue.
from collections import deque

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def size(self):
        return len(self.items)
    
    def reverse_k_elements(self, k):
        if k <= 0 or k > len(self.items):
            return "Invalid value of K"
        
        # Move the remaining elements in the queue to the end
        for _ in range(len(self.items) - k):
            self.items.append(self.items.pop(0))

    @staticmethod
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
    my_queue = Queue()

    # Enqueue elements
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)

    print("Queue:", my_queue.items)

    # Dequeue an element
    dequeued_item = my_queue.dequeue()
    print("Dequeued item:", dequeued_item)
    print("Queue after dequeue:", my_queue.items)

    # Check the size of the queue
    print("Size of the queue:", my_queue.size())
    my_queue.reverse_k_elements(3)
    print(my_queue.items)

    x = Queue.generate_binary_numbers(7)
    print(x)

