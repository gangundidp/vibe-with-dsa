class Solution:
    def findPrimeFactors(self, n):
        maxi = n + 1
        primes = [True] * (maxi + 1)
        
        primes[0] = primes[1] = False
        
        p = 2
        while p*p <= maxi:
            if primes[p]:
                for i in range(p*p, maxi + 1, p):
                    primes[i] = False
            p += 1
        
        res = []
        for i in range(1, int(n**0.5) + 1):
            if n%i == 0:
                if primes[i]:
                    res.append(i)
                if (n//i != i) and primes[n//i]:
                    res.append(n//i)
        return res

if __name__ == "__main__":
    sols = Solution()
    
    n = 13
    print("Output: ", sols.findPrimeFactors(n))
    
    n = 44
    print("Output: ", sols.findPrimeFactors(n))