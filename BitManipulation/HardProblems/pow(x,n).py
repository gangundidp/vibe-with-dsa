class Solution:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        
        if n%2 == 0:
            return self.pow(x*x, n//2)
        return x * self.pow(x, n - 1)

if __name__ == "__main__":
    sols = Solution()
    
    x = 2
    n = 6
    
    if n < 0:
        n = abs(n)
        res = sols.pow(x, n)
        print("output: ", 1/res)
    else:
        res = sols.pow(x, n)
        print("Output: ", res)