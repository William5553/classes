from LinkedList import LinkedList
from Array import Array
from Stack import Stack

list = [1, 2, 5, 7, 8, 3, 8, "a", "b", "8", 2, "f", 34.3, 75.2, "g", 22]

linked = LinkedList()
for item in list:
    linked.insertEnd(item)
print("\nLinked List:", linked)
linked.insert(3, "inserted")
linked.insertStart("start")
linked.insertEnd("end")
print(linked)

array = Array(len(list))
for i in range(len(list)):
    array[i] = list[i]
print("\nArray:", array)
array.insert(3, "inserted")
print(array)

stack = Stack()
for item in list:
    stack.push(item)
print("\nStack:", stack)
print(stack.pop(), stack)
print(stack.get(4), stack)