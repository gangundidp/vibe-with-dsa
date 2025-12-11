myStack = list()

print('My Stack: ', myStack)

myStack.append(1)
myStack.append(66)
myStack.append(93)

print('My Stack: ', myStack)
myStack.pop() # Removes last element
myStack.insert(1, 34) # add element at index 1

print('My Stack: ', myStack)
myStack.pop(1) # Removes element at index 1

print('My Stack: ', myStack)
myStack.remove(66)

print('My Stack: ', myStack)
myStack.pop()
myStack.pop() # throw error [IndexError]