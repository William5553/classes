class Stack:
    def __init__(self):
        self.items = []
    
    # adds an item to the top of the stack without using append
    def push(self, item):
        self.items = [item] + self.items
    
    # returns the top item on the stack and removes it (i = -1)
    def pop(self):
        top = self.items[0]
        self.items = self.items[1:]
        return top
    
    # returns the item at in index without removing it.
    def get(self, index):
        if index >= len(self.items):
            raise Exception("Index out of bounds")
        temp = Stack()
        for i in range(len(self.items)):
            temp.push(self.pop())
        item = temp.items[index]
        for i in range(len(temp.items)):
            self.push(temp.pop())
        return item

    # returns the top item on the stack without removing it
    def peek(self):
        return self.items[0]
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)