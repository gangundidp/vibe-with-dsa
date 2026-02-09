class Solution:
    def findXorTillN(self, n):
        if n%4 == 1:
            return  1
        if n%4 == 2:
            return n + 1
        if n%4 == 3:
            return 0
        return 4
    
    def findXorL_R(self, l, r):
        return self.findXorTillN(r) ^ self.findXorTillN(l-1) # l should not include

if __name__ == "__main__":
    l, r = 3, 5
    
    sol = Solution()
    ans = sol.findXorL_R(l, r)
    
    print(f"The XOR of numbers from {l} to {r} is: {ans}")