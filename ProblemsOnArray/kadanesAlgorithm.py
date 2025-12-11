from array import array as arr
from typing import *

class Solution:
    '''
    1. Iterate through the array using a variable i. During each iteration, add the current element arr[i] to a running sum variable.
    2. Keep track of the maximum sum encountered during the iteration by comparing the current sum with the previous maximum sum, and update it if the current sum is greater.
    3. If at any point the sum becomes negative, reset it to 0, as a negative sum won't contribute positively to the overall maximum sum.
    4. Continue the iteration until all elements in the array are processed.
    5. Finally, return the maximum sum encountered during the iteration.
    '''
    def maxSubarraySum(self, nums: List[int]) -> int:
        sum = 0
        maxSum = 0
        ans_start = ans_end = -1
        
        for i in range(len(nums)):
            if sum == 0:
                start = i
            sum += nums[i]

            if sum > maxSum:
                maxSum = sum
                ans_start = start
                ans_end = i
                
            if sum < 0:
                sum == 0
                
        return maxSum,nums[ans_start: ans_end+1] # plus +1, to include ans_end indexed element in the array
    
if __name__ == '__main__':
    sols = Solution()
    nums = arr('i', [2, 3, 5, -2, 7, -4])
    print('Maximum Subarray Sum: ', sols.maxSubarraySum(nums))
            