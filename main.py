import time
import random
from Array import Array
from Stack import Stack
from LinkedList import LinkedList

print("Array:\n======")
print("Insert Start:")
startTime = time.process_time()
myArr = Array(10000)
for i in range(10000):
  myArr.insert(i, 0)
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("Insert End:")
startTime = time.process_time()
myArr = Array(10000)
for i in range(10000):
  myArr.insert(i, len(myArr))
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("Random Access:")
myLen = len(myArr)
startTime = time.process_time()
for i in range(10000):
  myArr[random.randint(0, myLen-1)]
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("Random Insert:")
startTime = time.process_time()
for i in range(10000):
  myArr.insert(i, random.randint(0, myLen))
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("\nStack:\n======")
print("Push:")
startTime = time.process_time()
myStack = Stack()
for i in range(10000):
  myStack.push(i)
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("Pop:")
startTime = time.process_time()
for i in range(10000):
  myStack.pop()
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("Random Access:")
myStack = Stack()
for i in range(10000):
  myStack.push(i)
myLen = len(myStack)
startTime = time.process_time()
for i in range(10):
  myStack.get(random.randint(0,myLen-1))
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("\nLinked List:\n============")
print("Insert Start:")
startTime = time.process_time()
myLL = LinkedList()
for i in range(10000):
  myLL.insertStart(i)
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("Insert End:")
startTime = time.process_time()
myLL = LinkedList()
for i in range(10000):
  myLL.insertEnd(i)
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("Random Access:")
myLen = len(myLL)
startTime = time.process_time()
for i in range(10000):
  myLL.find(random.randint(0, myLen-1))
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)

print("Random Insert:")
startTime = time.process_time()
for i in range(10):
  myLL.insert(i, random.randint(0, myLen-1))
endTime = time.process_time()
print("Elapsed Time:", endTime-startTime)