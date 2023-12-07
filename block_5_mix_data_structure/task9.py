# 9. Write a method to merge two sorted linked lists into one sorted linked list.
# 10. Create a function that removes every Nth node from a linked list.

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

    @classmethod
    def merger_lst (cls, lst1, lst2):
        current = lst1.head
        while current.next:
            current = current.next
        current.next = lst2.head
    
    def rempver_nth(self, target):
        if not self.head:
            return

        if 1 == target:
            self.head = self.head.next
            return

        current = self.head
        cnt = 1
        while current.next:
            cnt += 1
            if cnt == target:
                current.next = current.next.next
                return
            current = current.next



linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(2)
linked_list_1.append(3)
linked_list_1.append(4)

linked_list_2 = LinkedList()
linked_list_2.append(5)
linked_list_2.append(6)
linked_list_2.append(7)
linked_list_2.append(8)


print("Linked Lists:")
linked_list_1.display()
linked_list_2.display()

LinkedList.merger_lst(linked_list_2, linked_list_1)
linked_list_2.display()
linked_list_1.display()

linked_list_2.rempver_nth(2)
linked_list_2.display()