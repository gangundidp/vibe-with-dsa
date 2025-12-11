from array import array as arr
from typing import *

class Solution:
    def upperBoundLinearSearch(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] > target:
                return i
        return len(nums)
    
    def upperBoundBinarySearch(self, target: int, low: int, high: int, nums: List[int]) -> int:
        ans = len(nums)
        
        while (low <= high):
            mid = (low + high)//2

            if nums[mid] < target:
                low = mid + 1
            else:
                ans = mid # upper bound means greater, here mid element is greater than target (nums[mid]>target)
                high = mid - 1
        return ans
                
    
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [1,2,2,3])
    print('Upper Bound: ', sols.upperBoundLinearSearch(2, nums))
    nums = arr('i', [3,5,8,9,15,19])
    print('Upper Bound: ', sols.upperBoundLinearSearch(9, nums))
    
    nums = arr('i', [1,2,2,3])
    print('Upper Bound: ', sols.upperBoundBinarySearch(2, 0, len(nums)-1, nums))
    nums = arr('i', [3,5,8,9,15,19])
    print('Upper Bound: ', sols.upperBoundBinarySearch(20, 0, len(nums)-1, nums))
