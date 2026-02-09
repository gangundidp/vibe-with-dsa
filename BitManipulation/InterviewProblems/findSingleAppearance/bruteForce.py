class Solution:
    def findSingleNumber(self, nums):
        res = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
            if cnt == 1:
                res.append(nums[i])
        return res
    
if __name__ == "__main__":
    nums = [1, 2, 3, 2, 1, 5]
    
    sols = Solution()
    res = sols.findSingleNumber(nums)

    print("Single time appearance nums: ", end='')
    for num in res:
        print(num, end=' ')
    
'''
Time Complexity: O(N*N), since nested for loops are used

Space Complexity: O(1). No extra space used
'''