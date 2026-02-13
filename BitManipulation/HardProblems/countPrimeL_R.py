class Solution:
    def countPrimes(self, queries):
        maxi = max(max(q) for q in queries)
        primes = [True] * (maxi + 1)
        
        primes[0] = primes[1] = False
        
        # print("primes: ", primes)
        p = 2
        while p*p <= maxi:
            if primes[p]:
                for i in range(p*p, maxi + 1, p):
                    primes[i] = False
            p += 1
            
        primes_count = [0] * (maxi + 1)
        for i in range(1, maxi + 1):
            primes_count[i] = primes_count[i - 1]
            if primes[i]:
                primes_count[i] += 1
            
        result = []
        for q in queries:
            start, end = q[0], q[1]
            if start == 0:
                result.append(primes_count[end])
            else:
                result.append(primes_count[end] - primes_count[start - 1])
        
        return result
                
    def main(self, arr):
        return self.countPrimes(arr)
            
if __name__ == "__main__":
    sols = Solution()
    arr = [ [2, 5], [4, 7] ]
    ans = sols.main(arr)
    print("Output: ", ans)