class Solution:
    # Recursive Approach
    def frogJump(self, heights, n):
        if n == 0:
            return 0
        
        l = self.frogJump(heights, n - 1) + abs(heights[n] - heights[n - 1])
        r = float("inf")
        if n > 1:
            r = self.frogJump(heights, n - 2) + abs(heights[n] - heights[n - 2])

        return min(l, r)
        
    def frogJumpMem(self, heights, n, dp):
        if n == 0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        one_jump = self.frogJumpMem(heights, n -1, dp) + abs(heights[n] - heights[n - 1])
        two_jumps = float("inf")
        if n > 1:
            two_jumps = self.frogJumpMem(heights, n -2, dp) + abs(heights[n] - heights[n - 2])

        dp[n] = min(one_jump, two_jumps)
        return dp[n]
        
    # Tabulation
    def frogJumpTab(self, heights, n):
        dp = [-1] * (n+1)
        dp[0] = 0 # Energy needed to climb first step is 0
        
        for i in range(1, n+1):
            oneStepAtTime = dp[i - 1] + abs(heights[i] - heights[i -1])
            twoStepsAtTime = float("inf")
            if i > 1:
                twoStepsAtTime = dp[i - 2] + abs(heights[i] - heights[i - 2])
            
            dp[i] = min(oneStepAtTime, twoStepsAtTime)
            
        return dp[n]


if __name__ == "__main__":
    sols = Solution()
    heights = [2, 1, 3, 5, 4]
    n = len(heights) - 1
    dp = [-1] * (n + 1)
    print("Output: ", sols.frogJump(heights, n))
    print("Output: ", sols.frogJumpMem(heights, n, dp))
    print("Output: ", sols.frogJumpTab(heights, n))
    
    heights = [7, 5, 1, 2, 6]
    dp = [-1] * (n + 1)
    print("Output: ", sols.frogJump(heights, n))
    print("Output: ", sols.frogJumpMem(heights, n, dp))
    print("Output: ", sols.frogJumpTab(heights, n))