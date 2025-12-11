from array import array as arr

class Solution:
    def findMissingRepeatingNumbers(self, arr):
        d = {}
        for ele in range(1, len(arr)+1):
            j = 0
            for i in range(len(arr)):
                if ele == arr[i]:
                    j += 1
            d[ele] = j
            
        t = []
        for k, v in d.items():
            if v == 2 or v == 0:
                t.append(k)
            
        return t,d
            
sols = Solution()
arr = arr('i', [1, 2, 3, 6, 7, 5, 7])
print("Output: ", sols.findMissingRepeatingNumbers(arr))