class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class StackLinkedList:
    def __init__(self):
        self.head = None # top index
        self.size = 0
    
    def push(self, x):
        # Create Node
        element = Node(x)
        # Set next pointer of node to top of stack's node
        element.next = self.head
        # set head(top) to top element of the stack
        self.head = element
        
        self.size += 1
        
    def pop(self):
        if self.head is None:
            return -1 # Empty  stack

        value = self.head.data
        tmp = self.head
        self.head = self.head.next
        del tmp
        self.size -= 1
        
    def top(self):
        if self.head is None:
            return -1
        
        return self.head.data
    
    def isEmpty(self):
        return self.size == 0
            
        

st = StackLinkedList()

# List of commands
commands = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
# List of inputs
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        st.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(st.pop(), end=" ")
    elif commands[i] == "top":
        print(st.top(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if st.isEmpty() else "false", end=" ")
    elif commands[i] == "LinkedListStack":
        print("null", end=" ")