# 6. Write a program that simulates a playlist using a linked list.

class Node:
    def __init__(self, composition):
        self.composition = composition
        self.next = None

    def __str__(self):
        return f"Data-{self.composition}, next -> {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, composition):
        new_node = Node(composition)
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
            print(current.composition, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    play_list = LinkedList()
    play_list.append("Sun")
    play_list.append("Morning")
    play_list.append("Night")
    play_list.append("4you")

    print("Linked List:")
    play_list.display()
    