class Solution:
    def maxSumOfAdjElements(self, idx, nums):
        if idx == 0:
            return nums[idx]

        if idx < 0:
            return 0
        
        left = nums[idx] + self.maxSumOfAdjElements(idx - 2, nums)
        right = 0 + self.maxSumOfAdjElements(idx - 1, nums)
        
        return max(left, right)
    
    # Memoization
    def maxSum(self, n, nums):
        dp = [-1] * n
        return self.solve(n - 1, nums, dp)

    def solve(self, n, nums, dp):
        if n == 0:
            return nums[n]
        
        if n < 1:
            return 0
        
        if dp[n] != -1:
            return dp[n]        

        pick = nums[n] + self.solve(n - 2, nums, dp)
        non_pick = 0 + self.solve(n - 1, nums, dp)
        
        dp[n] = max(pick, non_pick)
        return dp[n]
    
    
    # Tabulation
    def maxSumTab(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(len(nums)):
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
            non_pick = 0 + dp[i - 1] # Why 0? Not take current element
            
            dp[i] = max(pick, non_pick)
            
        return dp[len(nums)-1]
            
    
    
if __name__ == "__main__":
    sols = Solution()
    nums = [2, 1, 4, 9]
    print("Output: ", sols.maxSumOfAdjElements(len(nums) - 1, nums))
    print("Output: ", sols.maxSum(len(nums), nums))
    print("Output: ", sols.maxSumTab(nums))