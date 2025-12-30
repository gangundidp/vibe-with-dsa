class Solution:
    def findMaxDepthParenthesis(self, s):
        ans = 0
        max = 0
        
        for ch in s:
            if ch == '(':
                ans += 1
            elif ch == ')':
                ans -= 1
                
            if ans > max:
                max = ans
                
        return max
    
if __name__ == "__main__":
    sols = Solution()
    s = "(1+(2*3)+((8)/4))+1"
    print("Output: ", sols.findMaxDepthParenthesis(s))
    
    s = "(1)+((2))+((((3))))"
    print("Output: ", sols.findMaxDepthParenthesis(s))
    
                    