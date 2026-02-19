class Solution:
    def __init__(self):
        self.st = []
        self.size = 0
        
    def push(self, x):
        if not self.st:
            self.st.append((x, x))
            return
        minEle = min(self.getMin(), x)

        self.st.append((x, minEle))
        
        self.size += 1
        
    def pop(self):
        if not self.st:
            print("Empty Stack")
            return -1
        
        self.st.pop()
        
    def top(self):
        if not self.st:
            print("Empty Stack")
            return -1
        
        return self.st[-1][0]

    def getMin(self):
        return self.st[-1][1]
        
        
        
if __name__ == '__main__':
    s = Solution()
    
    # Function calls
    s.push(-2)
    s.push(0)
    s.push(-3)
    print("Stack: ", s.st)
    print("Min ele: ", s.getMin())
    s.pop()
    print("Stack: ", s.st)
    print("Top ele: ", s.top())
    s.pop()
    print("Min ele: ", s.getMin())