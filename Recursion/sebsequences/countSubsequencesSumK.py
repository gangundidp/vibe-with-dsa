from typing import *

'''
Problem Statement: Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.

'''

def countAllSubsequencesSumK(nums: List, idx: int, sum: int) -> int:
    if sum == 0:
        return 1
    
    if sum < 0 or idx >= len(nums):
        return 0
    
    return countAllSubsequencesSumK(nums, idx + 1, sum - nums[idx]) + countAllSubsequencesSumK(nums, idx + 1, sum)

nums = [4, 9, 2, 5, 1]
k = 5
print("Output: ", countAllSubsequencesSumK(nums, 0, k))