class Solution:
    def checkAnagram1(self, s, t):
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False
    
    def checkAnagram(self, s, t):
        ans = True
        if len(s) == len(t):
            for char in s:
                if s.count(char) != t.count(char):
                    ans = False
        else:
            return False
        return ans
    
    def checkAnagramByFreq(self, s, t):
        
        if len(s) != len(t):
            return False
        
        temp = [0] * 26
        for ch in s.upper():
            temp[ord(ch) - ord('A')] += 1
            
        for ch in t.upper():
            temp[ord(ch) - ord('A')] -= 1
            
        for count in temp:
            if count != 0:
                return False
        return True
    
if __name__ == "__main__":
    sols = Solution()
    s = "ABC"
    t = "CBA"
    print("Output: ", sols.checkAnagram(s, t))
    s = "tch"
    t = "pooo"
    print("Output: ", sols.checkAnagram(s, t))
    s = "level"
    t = "larel"
    print("Output: ", sols.checkAnagram(s, t))