from array import array as arr
from typing import *

# Finding Majority Element that repeated (n/2) times.
class Solution:
    # Time Com: O(n**2)
    def majorityElement(self, nums: List[int]) -> List[int]:
        majorityEle = None
        for ele in nums:
            cnt = 0
            for i in nums:
                if ele == i:
                    cnt += 1
                    
            if cnt >= (len(nums)//2):
                majorityEle = ele
                # break
                
        return majorityEle

    # Time Com: O(2n) and Space com: O(no. of Unique elements) or O(n) in worst case
    def majorityElementBetter(self, nums: List[int]) -> List[int]:
        counter = {}
        for ele in nums:
            if ele not in counter:
                counter[ele] = 1
            else:
                counter[ele] = counter[ele] + 1
        
        for key, value in counter.items():
            if value >= (len(nums)//2):
                return key
        return -1 # if no element more than n//2
    

if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [7, 0, 0, 1, 7, 7, 2, 2, 7, 7])
    # nums = arr('i', [7, 2, 2, 2, 7, 7, 2, 2, 7, 7]) # returns 7, last element
    # nums = arr('i', [7, 2, 2, 2, 7, 7, 2, 7, 7, 2]) # returns 2, last element
    print('Majority Element(n/2): ', sols.majorityElement(nums))
    print('Majority Element(n/2): ', sols.majorityElementBetter(nums))