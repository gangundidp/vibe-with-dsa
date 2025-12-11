from array import array as arr

class Solution:
    def findMaxConsecutiveOnes(self, arr):
        counter, max_ones = 0, 0
        for ele in arr:
            if ele == 0:
                if max_ones < counter:
                    max_ones = counter
                counter = 0
            else:
                counter += 1
        return max_ones
    
sols = Solution()
arr = arr('i',  [1, 1, 0, 0, 1, 1, 1, 0])
print('Max Consecutive Ones: ', sols.findMaxConsecutiveOnes(arr))