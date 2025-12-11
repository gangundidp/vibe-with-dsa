from queue import LifoQueue

myStack = LifoQueue()

print('My Stack: ', myStack)

myStack.put(3)
myStack.put(4)
myStack.put(5)
print('My Stack: ', myStack)

myStack.get()
myStack.get()
myStack.get()
print('My Stack: ', myStack)

# myStack.get() # waits for removing element from the empty stack
# myStack.get_nowait() # no waits
myStack.get(block=False)    # throws error
