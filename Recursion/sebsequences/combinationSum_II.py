from typing import *

class Solution:
    def combinationSumII(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()   # sorting to not include duplicate combinations
        ans = []
        temp = []
        self.solve(0, candidates, target, temp, ans)
        return ans
    
    def solve(self, idx: int, arr: List[int], target: int, temp: List[int], ans: List[int]):
        if (target == 0):
            ans.append(list(temp))
            return
        
        for i in range(idx, len(arr)):
            if i > idx and arr[i] == arr[i-1]:
                continue
            
            if arr[i] > target:
                break
            
            temp.append(arr[i])

            self.solve(i + 1, arr, target - arr[i], temp, ans)
            
            temp.pop()

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    sols = Solution()
    print("output: ", sols.combinationSumII(candidates, target))
    
    candidates = [2,5,2,1,2]
    target = 5
    sols = Solution()
    print("output: ", sols.combinationSumII(candidates, target))