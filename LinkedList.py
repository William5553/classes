class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    def insertEnd(self, value):
        newNode = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count