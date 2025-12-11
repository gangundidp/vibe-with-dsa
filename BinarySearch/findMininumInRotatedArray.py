from array import array as arr
from typing import *

class Solution:
    '''
    
    Given an integer array arr of size N, sorted in ascending order (with distinct values), the array is 
    rotated at any index which is unknown. Find the minimum element in the array.
    
    '''
    
    def findMinimumInRotatedArray(self, nums: List[int]) -> int:
        min_element = float('inf') 
        for i in range(len(nums)):
            if nums[i] < min_element:
                min_element = nums[i]
        return min_element
    
    def findMinimumInRotatedArrayUsingBinSearch(self, nums: List[int]) -> int:
        min_element = float('inf')
        low, high = 0, len(nums)-1
        
        while (low <= high):
            mid = low + (high - low)//2
            if (nums[mid] < min_element):
                min_element = nums[mid]

            if (nums[low] <= nums[mid]):
                if (nums[low] <= nums[mid] <= nums[mid+1]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (nums[mid] <= nums[high] <= nums[low]):
                    low = mid + 1
                else:
                    high = mid - 1
        return min_element
    
    def findMinimumInRotatedArrayUsingBin(self, nums: List[int]) -> int:
        min_element = float('inf')
        low, high = 0, len(nums)-1
        
        while (low <= high):
            mid = low + (high - low)//2
            if (nums[mid] < min_element):
                min_element = nums[mid]

            if (nums[mid] <= nums[high]):
                high = mid - 1
            else:
               low = mid + 1
                
        return min_element
    
    def striversAlgo(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        while (low < high):
            mid = low + (high - low)//2
            
            if (nums[mid] > nums[high]):
                low = mid + 1
            else:
                high = mid
                
        return nums[low]
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [3,4,5,1,2])
    print('Minimun Element: ', sols.findMinimumInRotatedArray(nums))
    nums = arr('i', [4,5,6,7,0,1,2,3])
    print('Minimun Element: ', sols.findMinimumInRotatedArray(nums))
    
    nums = arr('i', [3,4,5,1,2])
    print('Minimun Element: ', sols.findMinimumInRotatedArrayUsingBinSearch(nums))
    nums = arr('i', [4,5,6,7,0,1,2,3])
    print('Minimun Element: ', sols.findMinimumInRotatedArrayUsingBinSearch(nums))
    nums = arr('i', [4,5,-11,2,3])
    print('Minimun Element: ', sols.findMinimumInRotatedArrayUsingBinSearch(nums))
    
    nums = arr('i', [3,4,5,1,2])
    print('Minimun Element: ', sols.findMinimumInRotatedArrayUsingBin(nums))
    nums = arr('i', [4,5,6,7,0,1,2,3])
    print('Minimun Element: ', sols.findMinimumInRotatedArrayUsingBin(nums))
    nums = arr('i', [4,5,-11,2,3])
    print('Minimun Element: ', sols.findMinimumInRotatedArrayUsingBin(nums))
    
    nums = arr('i', [3, 4,5,6,7,0,1,2])
    print('Minimun Element: ', sols.striversAlgo(nums))
    