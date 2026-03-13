from collections import defaultdict

class Solution:
    def longestSubstr(self, s, k):
        n = len(s)
        res = 0
        freq = defaultdict(int)

        left = 0
        for right in range(n):
            freq[s[right]] += 1

            
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            res = max(res, right - left + 1)
        
        return res
    
    
    def longestSubstr2(self, s, k):
        n = len(s)
        res = 0
        freq = defaultdict(int)

        left = 0
        for right in range(n):
            freq[s[right]] += 1

            
            if len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            res = max(res, right - left + 1)
        
        return res
    
if __name__ == "__main__":
    sols = Solution()
    s = "aababbcaacc"
    k = 2
    print("Output: ", sols.longestSubstr(s, k))
    print("Output: ", sols.longestSubstr2(s, k))
    
    sols = Solution()
    s = "abcddefg"
    k = 3
    print("Output: ", sols.longestSubstr(s, k))
    print("Output: ", sols.longestSubstr2(s, k))

            