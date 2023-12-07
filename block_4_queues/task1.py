# 1. Implement a queue using arrays.
# 2. Write a program to enqueue an element into a queue.
# 3. Create a function to dequeue an element from a queue.
# 4. Implement a method to check if a queue is empty.
# 5. Write a function that returns the front element of a queue.


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
    
    def front_element(self):
        return self.items[0]

# Example usage
if __name__ == "__main__":
    my_queue = Queue()

    # Enqueue elements
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    print("Queue:", my_queue.items)

    # Dequeue an element
    dequeued_item = my_queue.dequeue()
    print("Dequeued item:", dequeued_item)
    print("Queue after dequeue:", my_queue.items)
    front_el = my_queue.front_element()
    print(f"Front element of queue is {front_el}")

    # Check the size of the queue
    print("Size of the queue:", my_queue.size())
