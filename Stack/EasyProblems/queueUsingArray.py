class ArrayQueue:
    def __init__(self, size = 10):
        self.queueArray = [0] * size
        self.start = -1
        self.end = -1
        self.currSize = -1
        self.maxSize = 10
        
    def push(self, x):
        if self.currSize == self.maxSize:
            print("Queue is full")
            return
        
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            # circular increment of end, why circular increment (% by maxSize) because to get end from starting when end becomes greater than maxSize
            self.end = (self.end + 1) % self.maxSize
        
        self.queueArray[self.end] = x
        self.currSize += 1
        
    def pop(self):
        # check for self.start instead of self.end, because in queue we pop element from the front
        if self.start == -1:
            print("Queue is Empty")
            return -1
        popped_ele = self.queueArray[self.start]

        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            # circular increment of start
            self.start = (self.start + 1) % self.maxSize
         
        self.currSize -= 1
        return popped_ele
    
    def peek(self):
        if self.start == -1:
            print("Queue is Empty")
            return
        return self.queueArray[self.start]
    
    def isEmpty(self):
        return self.currSize == 0
    
if __name__ == "__main__":
    queue = ArrayQueue()
    
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    print(queue.queueArray)

    print("popped element: ", queue.pop())
    print(queue.queueArray)

    print("Peek: ", queue.peek())