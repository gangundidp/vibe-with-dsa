from typing import *

class Solution:
    def solve(self, array: list, idx: int, target: int, temp: list, ans: list):
        if idx == len(array):
            if target == 0:
                ans.append(list(temp))
            return

        if array[idx] <= target:
            temp.append(array[idx])
            self.solve(array, idx, target - array[idx], temp, ans)
            temp.pop()
            
        
        self.solve(array, idx+1, target, temp, ans)
        
    def combinationSum(self, array: list, target: int):
        ans = []
        temp = []
        self.solve(array, 0, target, temp, ans)
        return ans
        
if __name__ == "__main__":
    array = [2, 3, 6, 7]
    target = 7
    sols = Solution()
    res = sols.combinationSum(array, target)
    print("output: ", res)
    
    array = [2]
    target = 2
    sols = Solution()
    res = sols.combinationSum(array, target)
    print("output: ", res)
