class Solution:
    def __init__(self):
        self.st = []
        self.minEle = float("inf")

    def push(self, val):
        if not self.st:
            self.st.append(val)
            self.minEle = val
            return
        
        if self.minEle < val:
            self.st.append(val)
        else:
            self.st.append(2 * val - self.minEle)
            self.minEle = val
        
    def pop(self):
        if not self.st:
            print("Empty stack")
            return -1
        
        popped_ele = self.st.pop()
        
        if popped_ele < self.minEle:
            self.minEle = 2 * self.minEle - popped_ele
            
    def top(self):
        if not self.st:
            return -1
        
        topEle = self.st[-1]

        if self.minEle < topEle:
            return topEle     # Return top if minimum is less than the top
        
        return self.minEle  # Otherwise return min
    
    def getMin(self):
        return self.minEle
    

if __name__ == "__main__":
    s = Solution()

    # Function calls
    s.push(-2)
    s.push(0)
    s.push(-3)
    print("Top: ", s.top())
    print("Stack: ", s.st)
    print("Min Ele: ", s.getMin())
    s.pop()
    print("Stack: ", s.st)
    print("Top: ", s.top())
    s.pop()
    print("Min Ele: ", s.getMin())