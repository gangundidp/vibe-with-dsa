from array import array

class Solution:
    def longestSubArray(self, arr, target):
        maxi = 0
        for i in range(len(arr)):
            sum = 0
            for j in range(i, len(arr)):
                sum += arr[j]
                if sum == target:
                    maxi = max(maxi, j - i + 1)

        return maxi
    
sols = Solution()
arr = array('i', [10, 5, 2, 7, 1, 9])             
print('Longest SubArray is: ', sols.longestSubArray(arr, 15))
arr = array('i', [-3, 2, 1])             
print('Longest SubArray is: ', sols.longestSubArray(arr, 6))
                    
        