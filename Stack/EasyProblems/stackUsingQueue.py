from queue import Queue

class QueueStack:
    def __init__(self, size = 10):
        self.stack = Queue()
        
    def isEmpty(self):
        return self.stack.empty()
        
    def push(self, x):
        s = self.stack.qsize()
        
        self.stack.put(x)

        # moving new element at front, so that it can at top
        for _ in range(s):
            self.stack.put(self.stack.get())
            
    def pop(self):
        # Get front element
        n = self.stack.queue[0]
        # remove front element
        self.stack.get()
        return n
    
    def top(self):
        return self.stack.queue[0]
    
if __name__ == "__main__":
    stack = QueueStack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.stack.queue)

    print("Top: ", stack.top())
    print("Popped Element: ", stack.pop())
    print(stack.stack.queue)
    
    print("Top: ", stack.top())