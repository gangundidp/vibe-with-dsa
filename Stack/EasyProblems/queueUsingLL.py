class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        
class QueueLL:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0
        
    def push(self, x):
        element = Node(x)

        if self.start is None:
            self.start = self.end = element
        else:
            self.end.next = element # updating the pointer
            self.end = element  # updating the end
            
        self.size += 1
        
    def pop(self):
        if self.start is None:
            return -1
        
        value = self.start.val  # Get the front value
        temp = self.start   # Store the front temporarily
        self.start = self.start.next    # Update front to next node
        del temp  # Delete old front node
        self.size -= 1
        
    def peek(self):
        if self.start is None:
            return -1
        
        return self.start.val
    
    def isEmpty(self):
        return self.size == 0
    

q = QueueLL()

# List of commands
commands = ["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"]
# List of inputs
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        q.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(q.pop(), end=" ")
    elif commands[i] == "peek":
        print(q.peek(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if q.isEmpty() else "false", end=" ")
    elif commands[i] == "LinkedListQueue":
        print("null", end=" ")
            