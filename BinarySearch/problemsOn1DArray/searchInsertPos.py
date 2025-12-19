from array import array as arr
from typing import *

class Solution:
    def searchInsertPosition(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return f'target present at index {i}'
            elif nums[i] > target:
                return i
        return len(nums) # returns lastIndex + 1, if target is greater than all element
    
    def searchInsertPositionBinSearch(self, target: int, low: int, high: int, nums: List[int]) -> int:
        ans = len(nums)
        while low <= high:
            mid = (low + high)//2
            
            if (nums[mid] == target):
                return f'target present at index {mid}'
            elif nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [1,2,4,7])
    print('Insert position: ', sols.searchInsertPosition(6, nums))
    nums = arr('i', [1,2,4,7])
    print('Insert position: ', sols.searchInsertPosition(2, nums))
    
    nums = arr('i', [1,2,4,7])
    print('Insert position: ', sols.searchInsertPositionBinSearch(6, 0, len(nums)-1, nums))
    nums = arr('i', [1,2,4,7])
    print('Insert position: ', sols.searchInsertPositionBinSearch(2, 0, len(nums)-1, nums))