from LinkedList import LinkedList
from Array import Array
from Stack import Stack

list = [1, 2, 5, 7, 8, 3, 8, "a", "b", "8", 2, "f", 34.3, 75.2, "g", 22]

linked = LinkedList()
for item in list:
    linked.insertEnd(item)
print(linked)

array = Array(len(list))
for i in range(len(list)):
    array[i] = list[i]
print(array)

stack = Stack()
for item in list:
    stack.push(item)
print(stack)