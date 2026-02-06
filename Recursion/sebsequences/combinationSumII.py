from typing import *

class Solution:
    def combinationSumII(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        self.solve(0, candidates, target, temp, ans)
        return ans
    
    def solve(self, ind: int, arr: List[int], target: int, temp: List[int], ans: List[int]):
        if ind == len(arr):
            if (target == 0) and (sorted(temp) not in ans): # sorting to not include duplicate combinations
                ans.append(sorted(temp))
            return
        
        if arr[ind] <= target:
            temp.append(arr[ind])
            self.solve(ind + 1, arr, target - arr[ind], temp, ans)
            temp.pop()
            
        self.solve(ind+1, arr, target, temp, ans)

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    sols = Solution()
    print("output: ", sols.combinationSumII(candidates, target))
    
    candidates = [2,5,2,1,2]
    target = 5
    sols = Solution()
    print("output: ", sols.combinationSumII(candidates, target))