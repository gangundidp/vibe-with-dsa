from array import array as arr
from typing import *

class Solution:
    '''
    
    Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. 
    The array is rotated at some pivot point that is unknown.
    Find the index at which k is present and if k is not present return -1.
    
    '''
    
    def searchElement(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
    def searchElementBinSearch(self, target: int, low: int, high: int, nums: List[int]) -> int:
        while (low <= high):
            mid = low + (high - low)//2
            
            if (nums[mid] == target):
                return mid
            
            if (nums[low] <= nums[mid]):
                if (nums[low] <= target <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (nums[mid] <= target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i',  [4, 5, 6, 7, 0, 1, 2])
    print('Output: ', sols.searchElement(0, nums))
    print('Output: ', sols.searchElement(3, nums))
    
    print('Output: ', sols.searchElementBinSearch(0, 0, len(nums)-1, nums))
    print('Output: ', sols.searchElementBinSearch(3, 0, len(nums)-1, nums))
    print('Output: ', sols.searchElementBinSearch(2, 0, len(nums)-1, nums))
    
    nums = arr('i',  [7, 8, 9, 1, 2, 3, 4, 5, 6])
    print('Output: ', sols.searchElementBinSearch(1, 0, len(nums)-1, nums))
    