from array import array as arr
from typing import *

class Solution:
    def linearSearch(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
    def binarySearch(self, target:int, low:int, high:int, nums: List[int]) -> int:
        mid = (low + high)//2
        # base condition
        if (low > high):
            return -1
        
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.binarySearch(target, low, mid-1, nums)
        elif target > nums[mid]:
            return self.binarySearch(target, mid+1, high, nums)
        
    def binarySearchIterative(self, target:int, low:int, high:int, nums: List[int]) -> int:
        while (low <= high):
            mid = (low+high)//2
            if (nums[mid] == target):
                return mid
            elif target < nums[mid]:
                high = mid -1
            else:
                low = mid + 1
        return -1
            

            
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [-1,0,3,5,9,12])
    target = 9
    print('Linear Search: ', sols.linearSearch(target, nums))
    print('Binary Search: ', sols.binarySearch(target, 0, len(nums)-1, nums))
    target = 9
    print('Binary Search: ', sols.binarySearchIterative(target, 0, len(nums)-1, nums))
        