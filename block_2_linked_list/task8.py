# 8. Write a method to find the middle element of a linked list.

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

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def search(self, target):
        current = self.head
        while current:
            # print("***", current, "***", current.data, "****", target)
            if current.data == target:
                return True
            current = current.next
        return False

    def delete(self, target):
        if not self.head:
            return

        if self.head.data == target:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return
            current = current.next

    def reverse_linked_list(self):
        current = self.head
        prev = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        linked_list.head = prev

    def find_middle_element(self):
        if self.head is None:
            return None
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer.data


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

    search_target = 3
    if linked_list.search(search_target):
        print(f"{search_target} found in the linked list.")
    else:
        print(f"{search_target} not found in the linked list.")

    delete_target = 2
    linked_list.delete(delete_target)
    print(f"Deleted {delete_target} from the linked list:")

    linked_list.display()

    cnt = linked_list.count_node()
    print("Count of nodes = ",cnt)

    new_node = 7
    linked_list.add_to_start(new_node)
    new_node = 8
    linked_list.add_to_end(new_node)
    linked_list.display()

    linked_list.reverse_linked_list()
    linked_list.display()

    midle = linked_list.find_middle_element()
    print(midle)