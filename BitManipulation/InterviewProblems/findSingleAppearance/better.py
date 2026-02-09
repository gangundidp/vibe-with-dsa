class Solution:
    def findSingleNumber(self, nums):
        maxi = max(nums)

        hash_map = [0] * (maxi+1)   # (maxi + 1) bcz to get maxi number index
        for num in nums:
            hash_map[num] += 1
            
        res = []
        for i in range(len(nums)):
            if hash_map[nums[i]] == 1:
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
Time Complexity: O(N)+O(N)+O(N), where N = size of the array. One O(N) is for finding the maximum, the second one is to hash the elements and the third one is to search the single element in the array.

Space Complexity: O(maxElement+1) where maxElement = the maximum element of the array.
'''