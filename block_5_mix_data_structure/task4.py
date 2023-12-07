# 4. Create a function that uses a stack to reverse the words in a sentence.

class Stack():
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def enequue(self, sentence):
        for liter in sentence:
            self.stack.insert(0, liter)
    
    def dequeue(self):
        sentence = ''.join(self.stack)
        return sentence
        

if __name__ == "__main__":
    my_stack = Stack()

    my_stack.enequue("Hello world")
    print(my_stack)

    rev_sentence = my_stack.dequeue()
    print(rev_sentence)