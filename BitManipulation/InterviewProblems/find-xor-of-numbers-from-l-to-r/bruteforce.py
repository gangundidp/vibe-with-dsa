class Solution:
    def findXorL_R(self, l, r):
        xor = 0
        for i in range(l, r+1): # r should include
            xor ^= i
        return xor
if __name__ == "__main__":
    l, r = 3, 5

    sol = Solution()

    ans = sol.findXorL_R(l, r)
    
    print(f"The XOR of numbers from {l} to {r} is: {ans}")