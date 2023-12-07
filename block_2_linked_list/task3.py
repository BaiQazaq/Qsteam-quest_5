# 3. Create a method to add a node at the beginning of a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Data-{self.data}, next -> {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def count_node(self):
        current = self.head
        cnt = 0
        while current:
            cnt += 1
            current = current.next
        return cnt
    
    def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("Linked List:")
    linked_list.display()

    cnt = linked_list.count_node()
    print("Count of nodes = ",cnt)

    new_node = 7
    linked_list.add_to_start(new_node)
    
    linked_list.display()