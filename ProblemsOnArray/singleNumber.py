from array import array as arr

class Solution:
    def singleNumber(self, arr):
        missingNUM = 0
        for ele in arr:
            missingNUM = missingNUM ^ ele
        return missingNUM
    
sols = Solution()
arr = arr('i', [1, 1, 2, 2, 3, 4, 4, 5, 5])
print("Missing number in twice numbers: ", sols.singleNumber(arr))