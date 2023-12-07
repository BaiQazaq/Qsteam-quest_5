# 6. Create a program to implement a circular queue.
# 8. Write a method to reverse the first K elements of a queue.

class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print(f"Control if func {(self.tail + 1) % self.k} = self.head = {self.head}")
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            print(f"Control befor self tail = {self.tail}")
            self.tail = (self.tail + 1) % self.k
            print(f"Control else func {(self.tail + 1) % self.k} and self.tail after = {self.tail}")
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

    def reverse_k_elements(self, k):
        if k <= 0 or k > len(self.queue):
            return "Invalid value of K"
        
        # Move the remaining elements in the queue to the end
        for _ in range(len(self.queue) - k):
            self.queue.append(self.queue.pop(0))


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(6)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()
obj.enqueue(10)

print("After adding an element to the queue")
obj.printCQueue()

obj.enqueue(11)

obj.reverse_k_elements(3)
obj.printCQueue()