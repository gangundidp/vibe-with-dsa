from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[] + nums[j] == target:
        #             return [i, j]
       
        nums.sort()
        left = 0
        right = len(nums) -1

        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left, right]

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
