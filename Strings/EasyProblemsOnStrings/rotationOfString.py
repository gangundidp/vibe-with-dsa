class Solution:
    def rotationOfString(self, s, t):
        i = 0
        
        while i < len(s):
            temp = s[i:] + s[0:i]
            if temp == t:
                return True
            i += 1
        return False
    
if __name__ == "__main__":
    sols = Solution()
    s = "rotation"
    t = "tionrota"
    print("Output: ", sols.rotationOfString(s, t))
    s = "hello"
    t = "lohelx"
    print("Output: ", sols.rotationOfString(s, t))