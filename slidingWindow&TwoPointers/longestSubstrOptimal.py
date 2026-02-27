class Solution:
    def longestSubstr(self, s):
        n = len(s)
        hash_map = [-1] * 256
        
        l, r, max_len = 0, 0, 0
        while r < n:
            
            if hash_map[ord(s[r])] != -1:
                l = max(hash_map[ord(s[r])] + 1, l) # Updating the left pointer

            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            hash_map[ord(s[r])] = r # storing the index
            r += 1
            
        return max_len
    

if __name__ == "__main__":
    sols = Solution()
    
    s = "abcddabac"
    print("Output: ", sols.longestSubstr(s))                
    s = "aab"
    print("Output: ", sols.longestSubstr(s))  