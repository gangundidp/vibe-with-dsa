class Solution:
    def minWindowSubstr(self, s: str, t):
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
        
        minLen = float("inf")
        start, end = 0, -1
        for i in range(len(s)):
            count = 0
            temp = freq.copy()
            for j in range(i, len(s)):
                if s[j] in temp and temp[s[j]] > 0:
                    count += 1
                    
                temp[s[j]] = temp.get(s[j], 0) - 1
                
                if count == len(t):
                    if minLen > j - i + 1:
                        minLen = j - i + 1
                        start = i
                        end = j
                    break
                
        return s[start:end + 1]
    
    def minWindowSubstrOptimal(self, s: str, t: str) -> str:
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
            
        count, left, right, minLen = 0, 0, 0, float("inf")
        start = 0
        end = - 1
        while right < len(s):
            if freq.get(s[right], 0) > 0:
                count += 1
            
            if s[right] in freq:
                freq[s[right]] = freq.get(s[right], 0) - 1
                
            
            while count == len(t):
                if s[left] in freq and freq[s[left]] <= 0:
                    freq[s[left]] += 1
                
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    start = left
                    end = right
                    
                if freq.get(s[left], 0) > 0:
                        count -= 1
                        
                left += 1
                
            right += 1
                
        return s[start:end + 1]
                
                
                
                

if __name__ == "__main__":
    sols = Solution()
    s = "ddaaabbca"
    t = "abc"
    
    print("Output: ", sols.minWindowSubstr(s, t))
    print("Output: ", sols.minWindowSubstrOptimal(s, t))

                    
    s = "ADOBEABCCODEBANC"
    t = "ABC"
    print("Output: ", sols.minWindowSubstr(s, t))
    print("Output: ", sols.minWindowSubstrOptimal(s, t))
    
    s = "a"
    t = "aa"
    print("Output: ", sols.minWindowSubstr(s, t))
    print("Output: ", sols.minWindowSubstrOptimal(s, t))

                    