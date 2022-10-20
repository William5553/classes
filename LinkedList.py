class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertEnd(self, data):
        newNode = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def delete(self, data): 
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return current
            previous = current
            current = current.next
        return None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count