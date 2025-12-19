from array import array as arr
from typing import *

class Solution:
    '''
    Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). 
    Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated.
    
    
    Imagine searching for the break in a long sorted belt by cutting it in halves repeatedly instead of scanning all the way through.
    Initialize low = 0 and high = n - 1.
    While low is less than high:
    Find mid index.
    If the element at mid is greater than the element at high, the rotation point is after mid, so update low = mid + 1.
    Else, the rotation point is at mid or before it, so update high = mid.
    When low meets high, that index is the rotation count (index of smallest element).
    '''
    def findNumberOfRotationsLinSearch(self, nums: List[int]) -> int:
        for i in range(1, len(nums) - 1):
            if nums[i-1] > nums[i]:
                return i
    

    def findNumberOfRotationsBinSearch(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while (low < high):
            mid = low + (high - low)//2
            if (nums[mid] > nums[high]):
                low = mid + 1
            else:
                high = mid
                
        return low  # smallest element index indicates no. of rotations
                
                
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [4, 5, 6, 7, 0, 1, 2, 3])
    print('No. of rotations: ', sols.findNumberOfRotationsLinSearch(nums))
    nums = arr('i', [3, 4, 5, 0, 1, 2])
    print('No. of rotations: ', sols.findNumberOfRotationsLinSearch(nums))
    
    nums = arr('i', [4, 5, 6, 7, 0, 1, 2, 3])
    print('No. of rotations: ', sols.findNumberOfRotationsBinSearch(nums))
    nums = arr('i', [3, 4, 5, 6, 7, 0, 1, 2])
    print('No. of rotations: ', sols.findNumberOfRotationsBinSearch(nums))