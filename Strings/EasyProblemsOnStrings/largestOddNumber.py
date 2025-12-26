class Solution:
    def largestOddNumber(self, s):
        i = len(s)-1
        res = ''
        
        while i >= 0:
            if int(s[i])%2 != 0:
                res = s[:i+1]
                break
            i -= 1
        
        j = 0
        
        while j <= i and s[j] == '0':
            j += 1
        
        return res[j:]
    
if __name__ == "__main__":
    sols = Solution()
    s = '5347'
    print("Output: ", sols.largestOddNumber(s))
    s = '0214638'
    print("Output: ", sols.largestOddNumber(s))
                
            