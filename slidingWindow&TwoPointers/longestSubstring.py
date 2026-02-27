class Solution:
    def longestSubstr(self, s):
        n = len(s)
        max_len = float("-inf")
        
        for i in range(n):
            
            hash_map = [0] * 256
            
            for j in range(i, n):
                if hash_map[ord(s[j])] == 1:
                    break
                
                curr_len = j - i + 1
                max_len = max(max_len, curr_len)
                hash_map[ord(s[j])] = 1
                
        return max_len

if __name__ == "__main__":
    sols = Solution()
    
    s = "abcddabac"
    print("Output: ", sols.longestSubstr(s))                
    s = "aab"
    print("Output: ", sols.longestSubstr(s))                
                