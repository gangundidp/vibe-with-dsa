class Solution:
    # Recursive Approach
    def fib1(self, n):
        if n <= 1:
            return n

        return self.fib1(n - 1) + self.fib1(n - 2)
    
    # DP: Memoization
    def fib2(self, n, dp):
        if n <= 1:
            return n

        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.fib2(n-1, dp) + self.fib2(n-2, dp)
        return dp[n]
    
    # Tabulation
    def fib3(self, n):
        if n <= 1:
            return n
        
        dp = [-1] * (n+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]

    
if __name__ == "__main__":
    sols = Solution()
    n = 5
    print("Fib using Recursion: ", sols.fib1(n))
    dp = [-1] * (n+1)
    print("Fib using DP (Memoization): ", sols.fib2(n, dp))
    print("Fib using DP (Tabulation): ", sols.fib3(n))