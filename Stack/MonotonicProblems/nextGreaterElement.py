from typing import *

#! Leetcode Problem 496
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            idx = nums2.index(num)
            next_greater = self.helper(idx, num, nums2)
            if next_greater:
                ans.append(next_greater)
            else:
                ans.append(-1)

        return ans

    def helper(self, idx, num, nums2):
        idx += 1
        while idx < len(nums2):
            if nums2[idx] > num:
                return nums2[idx]
            idx += 1
        return 0
    
if __name__ == "__main__":
    sols = Solution()
    
    nums1 = [4,1,2]
    nums2 = [1, 3, 4, 2]

    print("Output: ", sols.nextGreaterElement(nums1, nums2))