class Solution:
    def printDivisors(self, n):
        res = []
        for i in range(1, n+1):
            if n%i == 0:
                res.append(i)
        return res
    
    def printDivisorsOptimal(self, n):
        res = []
        for i in range(1, int(n**0.5)+1):
            if n%i == 0:
                res.append(i)
                if n//i != i:        
                    res.append(n//i)            
        return res
    
if __name__ == "__main__":
    sols = Solution()
    
    n = 36
    print("output: ", sols.printDivisors(n))
    n = 36
    print("output: ", sols.printDivisorsOptimal(n))