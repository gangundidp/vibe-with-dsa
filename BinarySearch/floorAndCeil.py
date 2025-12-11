from array import array as arr
from typing import *

class Solution:
    '''
    
    Problem Statement: ou're given an sorted array arr of n integers and an integer x. 
    Find the floor and ceiling of x in arr[0..n-1]. The floor of x is the largest element in the array 
    which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x
    
    '''
    def findFloorCeil(self, target: int, nums: List[int]) -> int:
        floor, ceil = float('-inf'), float('inf')

        for i in range(len(nums)):
            if nums[i] <= target and nums[i] >= floor:
                floor = nums[i]
            if nums[i] >= target and nums[i] <= ceil:
                ceil = nums[i]
                
        return floor, ceil
    
    def findFloorCeilBinSearch(self, target: int, low: int, high: int, nums: List[int]) -> int:
        while low <= high:
            mid = (low + high)//2
            
            if nums[mid] == target:
                # floor = ceil = mid
                return nums[mid], nums[mid]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return nums[high], nums[low], 
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [3, 4, 4, 7, 8, 10])
    print('Floor and Ceil: ', sols.findFloorCeil(5, nums))
    nums = arr('i', [3, 4, 4, 7, 8, 10])
    print('Floor and Ceil: ', sols.findFloorCeil(8, nums))
    
    nums = arr('i', [3, 4, 4, 7, 8, 10])
    print('Floor and Ceil: ', sols.findFloorCeilBinSearch(5, 0, len(nums)-1, nums))
    nums = arr('i', [3, 4, 4, 7, 8, 10])
    print('Floor and Ceil: ', sols.findFloorCeilBinSearch(8, 0, len(nums)-1, nums))