from array import array as arr
from typing import *

class Solution:
    def rearrangePositiveNegative(self, nums: List[int]) -> List[int]:
        positiveArray = []
        negativeArray = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                positiveArray.append(nums[i])
            else:
                negativeArray.append(nums[i])
                
        i = 0
        while i < len(nums) or i < len(nums):
            pass