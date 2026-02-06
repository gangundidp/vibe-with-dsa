from typing import *

class Solution:
    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
    def findLetterCombinations(self, digits: str):
        ans = []
        
        if not digits:
            return ans
        
        self.helper(digits, ans, 0, "")
        return ans
    
    def helper(self, digits: str, ans: List[str], idx: int, curr: str):
        if len(digits) == idx:
            ans.append(curr)
            return
        
        s = self.map[int(digits[idx])]

        for char in s:
            self.helper(digits, ans, idx + 1, curr + char)
            
if __name__ == "__main__":
    sols = Solution()
    digits = input("digits: ")
    print("Output: ", sols.findLetterCombinations(digits))