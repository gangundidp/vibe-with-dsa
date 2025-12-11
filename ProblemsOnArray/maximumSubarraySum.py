from array import array as arr
from typing import *

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                start = i
                sum += nums[j]
                if sum > maxSum:
                    maxSum = sum
                    arr_start = start
                    arr_end = j
                    
        return maxSum, nums[arr_start: arr_end+1]
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [2, 3, 5, -2, 7, -4])
    print("Maximum Subarray Sum: ", sols.maxSubarraySum(nums))