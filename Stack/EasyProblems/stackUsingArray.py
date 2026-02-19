from array import array as arr

class ArrayStack:
    def __init__(self, size = 1000):
        self.arrayStack = [0] * size
        self.capacity = size
        self.topIndex = -1
        
    def push(self, x):
        if self.topIndex >= self.capacity - 1:
            print("Stack Overflow")
            return
        self.topIndex += 1
        self.arrayStack[self.topIndex] = x
        
    def pop(self):
        if self.isEmpty():
            print("Empty Stack")
            return -1
        popped_ele = self.arrayStack[self.topIndex]
        self.topIndex -= 1
        return popped_ele
    
    def top(self):
        if self.isEmpty():
            print("Empty Stack")
            return -1
        return self.arrayStack[self.topIndex]

    def isEmpty(self):
        return self.topIndex == -1
            
            
if __name__ == "__main__":
    stack = ArrayStack(5)
    # arr = arr([2, 43, 489, 39, 20])

    stack.push(2)
    stack.push(43)
    stack.push(589)
    stack.push(5)
    print(stack.arrayStack)
    
    popped_ele = stack.pop()
    print('Popped Element: ', popped_ele)
    print(stack.arrayStack)

    print("Top: ", stack.top())

    