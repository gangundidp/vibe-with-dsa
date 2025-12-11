from array import array as arr
from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ele = None
        cnt = 0
        
        for i in range(n):
            if cnt == 0:
                ele = nums[i]
                cnt += 1
            elif nums[i] == ele:
                cnt += 1
            else: 
                cnt -= 1
                
        cnt1 = 0
        for i in range(n):
            if nums[i] == ele:
                cnt1 += 1
        if cnt1 >= (n//2):
            return ele
        return -1
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5])
    print('majority element: ', sols.majorityElement(nums))