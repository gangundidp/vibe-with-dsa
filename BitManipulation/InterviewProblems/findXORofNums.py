class Solution:
    def XORtillN(self, n):
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        if n % 4 == 3:
            return 0
        return n

    def findRangeXOR(self, l, r):
        return self.XORtillN(l - 1) ^ self.XORtillN(r)

if __name__ == "__main__":
    l, r = 3, 5
    sol = Solution()
    ans = sol.findRangeXOR(l, r)
    
    print(f"The XOR of numbers from {l} to {r} is: {ans}")
