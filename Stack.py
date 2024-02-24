class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to act as the stack

    def is_empty(self):
        return self.items == []  # Check if the stack is empty

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        return self.items.pop()  # Remove and return the top item of the stack

    def peek(self):
        return self.items[-1]  # Return the top item of the stack without removing it

    def size(self):
        return len(self.items)  # Return the number of items in the stack
    
