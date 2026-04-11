class Solution:
    # Recursion
    def frogJump(self, heights, n, k):
        if n == 0:
            return 0
        
        min_steps = float("inf")
        for i in range(1, k+1):
            if (n - i) >= 0:
                jumps = self.frogJump(heights, n - i, k) + abs(heights[n] - heights[n-i])
                min_steps = min(min_steps, jumps)
        return min_steps
    
    # Memoization
    def frogJumpMem(self, heights, n, k, dp):
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        
        min_steps = float("inf")
        for i in range(1, k+1):
            if (n - i) >= 0:
                jumps = self.frogJump(heights, n - i, k) + abs(heights[n] - heights[n-i])
                min_steps = min(min_steps, jumps)
        dp[n] = min_steps
        return min_steps
    
    def frogJumpTab(self, heights, n, k):
        dp = [-1] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            min_steps = float("inf")
            for j in range(1, k+1):
                if (i - j) >= 0:
                    jumps = dp[i - j] + abs(heights[i] - heights[i - j])
                    min_steps = min(min_steps, jumps)
                    
            dp[i] = min_steps
        return dp[n]
    
    
    
if __name__ == "__main__":
    sols = Solution()
    heights = [10, 5, 20, 0, 15]
    k = 2
    n = len(heights)
    dp = [-1] * n
    print("Output: ", sols.frogJump(heights, n-1, k))
    print("Output: ", sols.frogJumpMem(heights, n-1, k, dp))
    print("Output: ", sols.frogJumpTab(heights, n-1, k))
    print("=======================================")
    
    heights = [15, 4, 1, 14, 15]
    k = 3
    n = len(heights)
    dp = [-1] * n
    print("Output: ", sols.frogJump(heights, n-1, k))
    print("Output: ", sols.frogJumpMem(heights, n-1, k, dp))
    print("Output: ", sols.frogJumpTab(heights, n-1, k))