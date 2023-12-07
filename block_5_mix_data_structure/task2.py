# 2. Implement a text editor undo feature using stacks.

class TextEditor:
    def __init__(self):
        self.text_stack = []  # Stack for the current state of the text
        self.undo_stack = []  # Stack for undo history

    def insert_text(self, text):
        # Insert text and push the current state onto the text stack
        self.text_stack.append(text)
        # Clear the undo stack since a new action is performed
        self.undo_stack = []

    def undo(self):
        if len(self.text_stack) > 1:
            # Pop the current state from the text stack
            self.undo_stack.append(self.text_stack.pop())
            # Restore the previous state as the current state
            current_state = self.text_stack[-1]
            # Push the undone state onto the text stack
            self.text_stack.append(self.undo_stack.pop())
            return current_state
        else:
            return self.text_stack[0]

# Example usage
if __name__ == "__main__":
    editor = TextEditor()

    editor.insert_text("Hello, ")
    print("Current Text:", editor.text_stack[-1])

    editor.insert_text("World!")
    print("Current Text:", editor.text_stack[-1])

    undo_result = editor.undo()
    print("Undo Result:", undo_result)
    print("Current Text:", editor.text_stack[-1])

    undo_result = editor.undo()
    print("Undo Result:", undo_result)
    print("Current Text:", editor.text_stack[-1])
