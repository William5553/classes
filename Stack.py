class Stack:
    def __init__(self):
        self.items = []
    
    # adds an item to the top of the stack
    def push(self, item):
        self.items.append(item)
    
    # returns the top item on the stack and removes it
    def pop(self):
        return self.items.pop()
    
    # returns the top item on the stack without removing it
    def peek(self):
        return self.items[len(self.items)-1]
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)