class Solution:
    # recursion
    def climbingStairsRec(self, n):
        if n <= 1:
            return 1
        left = self.climbingStairsRec(n - 1)
        right = self.climbingStairsRec(n - 2)
        return left + right
    
    # Memoization
    def climbingStairMem(self, n):
        if n <= 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[n] = self.helper(dp, n - 1) + self.helper(dp, n-2)
        return dp[n]

    def helper(self, dp, n):
        if n <= 1:
            return 1
        
        if dp[n] != 0:
            return dp[n]
        
        dp[n] = self.helper(dp, n - 1) + self.helper(dp, n-2)
        return dp[n]
    
    
    # Tabulation
    def climbingStairs(self, n):
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
if __name__ == "__main__":
    sols = Solution()

    n = 2
    print("Output: ", sols.climbingStairsRec(n))
    print("Output: ", sols.climbingStairMem(n))
    print("Output: ", sols.climbingStairs(n))
    
    n = 3
    print("Output: ", sols.climbingStairsRec(n))
    print("Output: ", sols.climbingStairMem(n))
    print("Output: ", sols.climbingStairs(n))
    
    n = 4
    print("Output: ", sols.climbingStairsRec(n))
    print("Output: ", sols.climbingStairMem(n))
    print("Output: ", sols.climbingStairs(n))