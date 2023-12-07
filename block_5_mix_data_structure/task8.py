# 8. Implement a customer service simulation using queues.

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
        
    def display(self):
        cnt = 1
        for item in self.items:
            print(f"{cnt} - {item}")
            cnt += 1
        
    
    def size(self):
        return print(f"{len(self.items)} activities on queue")


    @staticmethod
    def input_item():
        item = input("Enter the item to add to the queue -> ")
        return item

queue = Queue()
cmd = """
Next command avalable:
1. Add item to queue
2. Remove item from queue
3. Display queue
4. Show size of queue
"""

while True:
    res = queue.is_empty()
    if res == True:
        print("Queue is empty, lets start")
        item = Queue.input_item()
        queue.enqueue(item)
    else:
        print(cmd)
        user_cmd = input("Enter only number of command -> ")
        match user_cmd:
            case "1":
                item = Queue.input_item()
                queue.enqueue(item)
            case "2":
                item = queue.dequeue()
                print(f"Was deleted \"{item}\" item from queue")
            case "3":
                queue.display()
            case "4":
                queue.size()
            case _:
                print("Wrong command")
        


# # Example usage
# if __name__ == "__main__":
#     my_queue = Queue()

#     # Enqueue elements
#     my_queue.enqueue(1)
#     my_queue.enqueue(2)
#     my_queue.enqueue(3)
#     my_queue.enqueue(4)
#     my_queue.enqueue(5)

#     print("Queue:", my_queue.items)

#     # Dequeue an element
#     dequeued_item = my_queue.dequeue()
#     print("Dequeued item:", dequeued_item)
#     print("Queue after dequeue:", my_queue.items)

    
