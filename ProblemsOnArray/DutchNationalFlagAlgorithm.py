from array import array as arr
from typing import *

class Solution:
    def sortZeroesOnesTwos(self, nums: List[int]) -> List[int]:
        low, mid, high = 0, 0, len(nums)-1
        
        while (mid <= high):
            if (nums[mid] == 0):
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif (nums[mid] == 1):
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
        return nums
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [0, 2, 2, 1, 0, 1, 0, 2])
    print("Sorted array: ", sols.sortZeroesOnesTwos(nums))