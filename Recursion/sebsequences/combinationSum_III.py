from typing import *

class Solution:
    def combinationSumIII(self, curr: int, k: int, n: int, temp: List[int], res: List[List[int]]):
        if len(temp) == k and n == 0:
            res.append(list(temp))
            return
        
        if len(temp) == k and n > 0:
            return

        if curr <= n:
            temp.append(curr)
            self.combinationSumIII(curr + 1, k, n - curr, temp, res)
            temp.pop()
            self.combinationSumIII(curr + 1, k, n, temp, res)
        else:
            return

if __name__ == "__main__":
    sols = Solution()
    k, n = 3, 7
    res = []
    temp = []
    sols.combinationSumIII(1, k, n, temp, res)
    print("output: ", res)
    
    k, n = 3, 9
    res = []
    temp = []
    sols.combinationSumIII(1, k, n, temp, res)
    print("output: ", res)