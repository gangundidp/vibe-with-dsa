from collections import deque

myStack = deque()

print('My Stack: ', myStack)

myStack.append(1)
myStack.append(66)
myStack.append(93)

print('My Stack: ', myStack)
myStack.pop() # Removes last element
myStack.insert(1, 34) # add element at index 1

# myStack.pop(1) # throw error , deque pop method takes no arguments

print('My Stack: ', myStack)
myStack.remove(66)

myStack.popleft() # removes 1st element from front, works like queue
print('My Stack: ', myStack)
myStack.pop()
myStack.pop() # throw error [IndexError]