class Solution:
    def threeSum(self, nums):
        lst = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        if (i != j!= k):
                            lst.append([nums[i], nums[j], nums[k]])
        return lst
    def threeSumBetter(self, nums):
        lst = []
        for i in range(len(nums)):
            for j in range(i, len(nums)-1):
                if (nums[i] + nums[j] + nums[j+1]  == 0) and (i != j != j+1):
                    lst.append([nums[i], nums[j], nums[j+1]])
                    
        return lst
                    
    
sols = Solution()
nums = [-1,0,1,2,-1,-4]
print('Output: ', sols.threeSum(nums))
print('Output: ', sols.threeSumBetter(nums))