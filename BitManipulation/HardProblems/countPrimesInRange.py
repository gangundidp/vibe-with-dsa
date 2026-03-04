class Solution:
    def countPrimesInRange(self, n):
        res = []
        for i in range(1, int(n**0.5) + 1):
            if n%i == 0:
                if self.is_prime(i):
                    res.append(i)
                if (n//i != i) and self.is_prime(n//i):
                    res.append(n//i)
            # print(i, res)
        return res
    
    def is_prime(self, n):
        if n <= 1:
            return False
        p = 2
        while p*p <= n:
            if n%p == 0:
                return False
            p += 1
        return True
    
if __name__ == "__main__":
    sols = Solution()
    n = 13
    print("output: ", sols.countPrimesInRange(n))
    
    n = 6
    print("output: ", sols.countPrimesInRange(n))