from array import array as arr
from typing import *

class Solution:
    '''
    
    Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values)
    and a target value k. Now the array is rotated at some pivot point unknown to you. 
    Return True if k is present and otherwise, return False.
    
    '''
    
    def searchElementInRotatedArray(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False
    
    def searchElementInRotatedArrayBinSearch(self, target: int, low: int, high: int, nums: List[int]) -> int:
        while (low <= high):
            mid = low + (high - low)//2
            
            if (nums[mid] == target):
                return True
            
             # Cannot determine sorted half due to duplicates
            if (nums[low] == nums[mid] == nums[high]):
                low += 1
                high -= 1
                continue
            
            # left half is sorted
            if (nums[low] <= nums[mid]):
                if (nums[low] <= target <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            # right half is sorted
            else:
                if (nums[mid] <= target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        return False
            
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [7, 8, 1, 2, 3, 3, 3, 4, 5, 6])
    print(f'Output: {sols.searchElementInRotatedArray(3, nums)}')
    print(f'Output: {sols.searchElementInRotatedArray(10, nums)}')
    
    print(f'Output: {sols.searchElementInRotatedArrayBinSearch(3, 0, len(nums)-1, nums)}')
    print(f'Output: {sols.searchElementInRotatedArrayBinSearch(10, 0, len(nums)-1, nums)}')
    
    nums = arr('i',  [4, 5, 6, 7, 0, 1, 2, 2, 2])
    print(f'Output: {sols.searchElementInRotatedArrayBinSearch(0, 0, len(nums)-1, nums)}')
    print(f'Output: {sols.searchElementInRotatedArrayBinSearch(10, 0, len(nums)-1, nums)}')