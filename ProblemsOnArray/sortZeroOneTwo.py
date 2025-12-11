from typing import List

class Solution:
    def sortZeroOneTwo(self, nums: List[int]):
        no_of_zeroes, no_of_ones, no_of_twos = 0, 0, 0
        for num in nums:
            if num == 0:
                no_of_zeroes += 1
            elif num == 1:
                no_of_ones += 1
            elif num == 2:
                no_of_twos += 1
        
        for i in range(len(nums)):
            if i < no_of_zeroes:
                nums[i] = 0
            elif i < no_of_ones + no_of_zeroes:
                nums[i] = 1
            else:
                nums[i] = 2
                
        return nums
    
sols = Solution()
nums = [1, 0, 2, 1,1, 0]
print('Sorted array: ', sols.sortZeroOneTwo(nums))