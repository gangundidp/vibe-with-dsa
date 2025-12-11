from array import array as arr
from typing import *

class Solution:
    '''
    Problem Statement: Given an array of length N, peak element is defined as the element greater than both of its neighbors.
    Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. 
    Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index 
    of any peak number.
    
    Examples
    Input: arr[] = {1,2,3,4,5,6,7,8,5,1}
    Output: 7
    Explanation: There is only 1 peak element, 8,  that is at index 7.

    Input: arr[] = {1,2,1,3,5,6,4} 
    Output: 1 
    Explanation : There are 2 peak numbers that are at indices 1 and 5. We can return any of them.
                
    '''
    
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1, len(nums)-2):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
            
    def findPeakElementBinSearch(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        while (low <= high):
            mid = low + (high - low)//2
            
            if (nums[mid-1] < nums[mid] > nums[mid+1]):
                return mid
            
            if (nums[mid] >= nums[mid-1]):
                low = mid + 1
            elif (nums[mid] >= nums[mid+1]):
                high = mid - 1
                
        return -1

if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [1, 2, 1, 3, 5, 6, 4])
    print('Peak Element Index: ', sols.findPeakElement(nums))
    
    nums = arr('i', [1, 2, 1, 3, 5, 6, 7])
    # nums = arr('i', [1,2,3,4,5,6,7,8,5,1])
    print('Peak Element Index: ', sols.findPeakElementBinSearch(nums))
    
    