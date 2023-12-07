# 1. Write a program to solve the Tower of Hanoi problem using stacks.

class Stack:
    def __init__(self):
        self.A = []
        self.B = []
        self.C = []

    
    def is_empty(self, stack):
        return len(stack) == 0

    def push(self, item, stack):
        stack.insert(0, item)

    def pop(self, stack):
        if not self.is_empty(stack):
            return stack.pop(0)
        else:
            raise IndexError("pop from an empty stack")
   
    def rebuild_tower(self, n, stackA, stackB, stackC):
        if n==1:
            x = self.pop(stackA)
            self.push(x, stackC)
            print(f"stack A - {stack.A}                 stack B - {stack.B}          stack C - {stack.C}")
            self.rebuild_tower(n-1, stackA, stackB, stackC)
        elif n == 2:
            x = self.pop(stackB)
            self.push(x, stackC)
            print(f"stack A - {stack.A}              stack B - {stack.B}          stack C - {stack.C}")
            self.rebuild_tower(n-1, stackA, stackB, stackC)
        elif n == 3:
            x = self.pop(stackB)
            self.push(x, stackA)
            print(f"stack A - {stack.A}              stack B - {stack.B}      stack C - {stack.C}")
            self.rebuild_tower(n-1, stackA, stackB, stackC)
        elif n == 4:
            x = self.pop(stackA)
            self.push(x, stackC)
            print(f"stack A - {stack.A}                 stack B - {stack.B} stack C - {stack.C}")
            self.rebuild_tower(n-1, stackA, stackB, stackC)
        elif n == 5:
            x = self.pop(stackC)
            self.push(x, stackB)
            print(f"stack A - {stack.A}            stack B - {stack.B} stack C - {stack.C}")
            self.rebuild_tower(n-1, stackA, stackB, stackC)
        elif n == 6:
            x = self.pop(stackA)
            self.push(x, stackB)
            print(f"stack A - {stack.A}            stack B - {stack.B}      stack C - {stack.C}")
            self.rebuild_tower(n-1, stackA, stackB, stackC)
        elif n == 7:
            x = self.pop(stackA)
            self.push(x, stackC)
            print(f"stack A - {stack.A}      stack B - {stack.B}          stack C - {stack.C}")
            self.rebuild_tower(n-1, stackA, stackB, stackC)
        
         

stack = Stack()
stack.push("***", stack.A)
stack.push("**", stack.A)
stack.push("*", stack.A)

print(f"stack A - {stack.A} stack B - {stack.B}          stack C - {stack.C}")

# Driver code
n = 7
Stack().rebuild_tower(n, stack.A, stack.B, stack.C) 
print(f"stack A - {stack.A}                 stack B - {stack.B}          stack C - {stack.C}")