from array import array as arr
from typing import *

class Solution:
    '''
    Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

    Examples
    Input : arr[] = {1,1,2,2,3,3,4,5,5,6,6}
    Output: 4
    Explanation: Only the number 4 appears once in the array.

    Input: arr[] = {1,1,3,5,5}
    Output : 3
    Explanation: Only the number 3 appears once in the array.

    '''
    
    def findSingleElementLinSearch(self, nums: List[int]) -> int:
        for i in range(1, len(nums), 2):
            if nums[i-1] != nums[i]:
                return nums[i-1]
        return -1
    
    def findSingleElementXor(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            ans = ans ^ nums[i]
        
        if (ans in nums):
            return ans
        return -1
    
    def findSingleElementBinSearch(self, nums: List[int]) -> int:
        n = len(nums)
        if (len(nums) == 1):
            return nums[0]
        elif (nums[0] != nums[1]):
            return nums[0]
        elif (nums[n-1] != nums[n-2]):
            return nums[n-1]
        elif (len(nums)%2 == 0):
            return -1

        low, high = 1, n-2
        while (low <= high):
            mid = low + (high - low)//2
            
            if (nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]):
                return mid

            if ((mid%2 == 0) and  nums[mid] == nums[mid+1]) or ((mid%2 != 0) and nums[mid] == nums[mid-1]):
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6])
    print('Single Element: ', sols.findSingleElementLinSearch(nums))
    nums = arr('i', [1, 1, 2, 2, 3, 5, 5])
    print('Single Element: ', sols.findSingleElementLinSearch(nums))
    nums = arr('i', [1, 1, 2, 2, 3, 3, 5, 5])
    print('Single Element: ', sols.findSingleElementLinSearch(nums))
    
    nums = arr('i', [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6])
    print('Single Element: ', sols.findSingleElementXor(nums))
    nums = arr('i', [1, 1, 2, 2, 3, 3, 5, 5])
    print('Single Element: ', sols.findSingleElementXor(nums))
    
    nums = arr('i', [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6])
    print('Single Element: ', sols.findSingleElementBinSearch(nums))
    nums = arr('i', [1, 1, 2, 2, 3, 5, 5])
    print('Single Element: ', sols.findSingleElementBinSearch(nums))