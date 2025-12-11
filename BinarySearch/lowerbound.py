from array import array as arr
from typing import *

class Solution:
    def lowerBoundUsingBinSearch(self, target:int, low:int, high:int, nums: List[int]) -> int:
        mid = (low + high)//2
        if (low > high):
            if (low == len(nums)):
                return len(nums)
            else:
                if (nums[low] > target):
                    return low
                else:
                    return low+1

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.lowerBoundUsingBinSearch(target, low, mid-1, nums)
        elif target > nums[mid]:
            return self.lowerBoundUsingBinSearch(target, mid+1, high, nums)
        
    def lowerBoundUsingLinSearch(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)

        
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [1,2,2,3])
    print('Lower Bound: ', sols.lowerBoundUsingBinSearch(2, 0, len(nums)-1, nums))
    nums = arr('i', [3,5,8,15,19])
    print('Lower Bound: ', sols.lowerBoundUsingBinSearch(9, 0, len(nums)-1, nums))
    nums = arr('i', [1,2,2,3])
    print('Lower Bound: ', sols.lowerBoundUsingLinSearch(2, nums))
    nums = arr('i', [3,5,8,15,19])
    print('Lower Bound: ', sols.lowerBoundUsingLinSearch(9, nums))