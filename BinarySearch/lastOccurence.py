from array import array as arr
from typing import *

class Solution:
    '''
    
    Problem Statement: Given a sorted array of N integers, write a program to find the index of the last 
    occurrence of the target key. If the target is not found then return -1. Note: Consider 0 based indexing
    
    '''
    
    def lastOccurenceLinSearch(self, target: int, nums: List[int]) -> int:
        last_occurence = -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                last_occurence = i
                
        return last_occurence
    
    def lastOccurenceBinSearch(self, target: int, low: int, high: int, nums: List[int]) -> int:
        last_occurence  = -1
        
        while (low <= high):
            mid = low + (high - low)//2
            if (nums[mid] == target):
                last_occurence = mid 
                low = mid + 1
            elif (nums[mid] > target):
                high = mid - 1
            else: 
                low = mid + 1
                
        return last_occurence
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [3, 4, 13, 13, 13, 13, 20, 40])
    print('Last Occurence: ', sols.lastOccurenceLinSearch(13, nums))
    nums = arr('i', [3, 4, 13, 13, 13, 20, 40])
    print('Last Occurence: ', sols.lastOccurenceLinSearch(60, nums))
    
    nums = arr('i', [3, 4, 13, 13, 13, 13, 20, 40])
    print('Last Occurence: ', sols.lastOccurenceBinSearch(13, 0, len(nums)-1, nums))
    nums = arr('i', [3, 4, 13, 13, 13, 20, 40])
    print('Last Occurence: ', sols.lastOccurenceBinSearch(60, 0, len(nums)-1, nums))