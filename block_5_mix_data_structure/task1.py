# 1. Create a program that uses both a stack and a queue to print elements in alternating order.

class MixedStackQueue():
    def __init__(self):
        self.stack = []
        self.queue = []

    def is_empty(self, lst):
        return len(lst) == 0

    def enqueue(self, item):
        self.stack.insert(0, item)
        self.queue.append(item)

    def dequeue(self, lst):
        if not self.is_empty(lst):
            return lst.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def size(self, lst):
        return len(lst)
    

if __name__ == "__main__":
    my_items = MixedStackQueue()

    # Enqueue elements
    my_items.enqueue(1)
    my_items.enqueue(2)
    my_items.enqueue(3)
    my_items.enqueue(5)
    my_items.enqueue(6)

    print(f"Stack - {my_items.stack}")
    print(f"Queue - {my_items.queue}")

    dequeued_item = my_items.dequeue(my_items.stack)
    print(f"Dequeued item:", dequeued_item)
    print("Stack after dequeue:", my_items.stack)

    dequeued_item = my_items.dequeue(my_items.queue)
    print(f"Dequeued item:", dequeued_item)
    print("Stack after dequeue:", my_items.queue)
