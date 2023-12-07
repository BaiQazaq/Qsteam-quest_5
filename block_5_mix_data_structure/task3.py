# 3. Write a program to implement two stacks in one array.


class TwoStacks():
    position = ["head", "tail"]
    def __init__(self) -> None:
        self.stack = []
        self.cnt_front = 0
        self.cnt_back = 0

    def is_empty(self):
        return len(self.stack) == 0

    def enqueue(self, item, position):
        if position == 'head':
            self.stack.insert(0, item)
            self.cnt_front += 1
        elif position == "tail":
            self.stack.append(item)
            self.cnt_back -= 1

    def dequeue(self, position):
        if not self.is_empty():
            if position == "head" and self.cnt_front > 0:
                self.cnt_front -= 1
                return self.stack.pop(0), 
            elif position == "head" and self.cnt_front <= 0:
                print("Head stack empty")
            if position == "tail" and self.cnt_back < 0:
                self.cnt_back += 1
                return self.stack.pop(-1)
            elif position == "tail" and self.cnt_back >= 0:
                 print("Tail stack empty")
        else:
            raise IndexError("Stack an empty")

    def size(self, lst):
        return len(lst)
    

if __name__ == "__main__":
    my_items = TwoStacks()


    my_items.enqueue(1, TwoStacks.position[0])
    my_items.enqueue(2, TwoStacks.position[1])
    my_items.enqueue(3, TwoStacks.position[0])
    my_items.enqueue(4, TwoStacks.position[1])
    my_items.enqueue(5, TwoStacks.position[0])
    my_items.enqueue(6, TwoStacks.position[1])
    my_items.enqueue(7, TwoStacks.position[0])
    my_items.enqueue(8, TwoStacks.position[1])

    print(f'Initaial stack - {my_items.stack}')

    my_items.dequeue(TwoStacks.position[0])
    my_items.dequeue(TwoStacks.position[1])

    print(f'Stack after dequeue - {my_items.stack}')

    

