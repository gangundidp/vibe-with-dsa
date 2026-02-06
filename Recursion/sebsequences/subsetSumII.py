from typing import *

class Solution:
    def subsetSumII(self, idx: int, arr: List[int], curr: List[int], res: List[List[int]]):
        if idx == len(arr):
            if (curr not in res):
                res.append(list(curr))
            return
        
        self.subsetSumII(idx + 1, arr, curr, res)
        curr.append(arr[idx])
        self.subsetSumII(idx + 1, arr, curr, res)
        
        curr.pop()
        
if __name__ == "__main__":
    arr = [1, 2, 2]
    res = []
    sols = Solution()
    sols.subsetSumII(0, arr, [], res)
    print("output: ", res)
    
    arr = [1]
    res = []
    sols = Solution()
    sols.subsetSumII(0, arr, [], res)
    print("output: ", res)
