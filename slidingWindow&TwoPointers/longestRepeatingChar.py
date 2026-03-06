class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0 
        
        for i in range(len(s)):
            freq = [0] * 26
            
            max_freq = 0
            
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('A')] += 1
                
                max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])

                windowLen = j - i + 1
                
                replace = windowLen - max_freq
                
                if replace <= k:
                    maxLength = max(maxLength, windowLen)
        return maxLength

    def characterReplacementBetter(self, s: str, k: int) -> int:
        freq = {}

        max_freq = 0
        maxLen = 0
        
        left = 0
        for right in range(len(s)):
            # Increase frequency of current character
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            # Update the max frequency in current window
            max_freq = max(max_freq, freq[s[right]])
            
             # If window is invalid (more than k replacements)
            while ((right - left + 1) - max_freq) > k:
                freq[s[left]] -= 1
                left += 1
            
            # Update max_len with current valid window size
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
    
    def characterReplacementOptimal(self, s: str, k: int) -> int:
        freq = [0] * 26

        max_freq = 0
        maxLen = 0
        
        left = 0
        for right in range(len(s)):
            # Increase frequency of current character
            freq[ord(s[right]) - ord('A')] += 1
            
            # Update the max frequency in current window
            max_freq = max(max_freq, freq[ord(s[right]) - ord('A')])
            
             # If window is invalid (more than k replacements)
            while ((right - left + 1) - max_freq) > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            # Update max_len with current valid window size
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
    
    
if __name__ == "__main__":
    sol = Solution()
    s = "AABABBA"
    k = 1
    # Output: 4
    print("Output: ", sol.characterReplacement(s, k)) 
    print("Output: ", sol.characterReplacementBetter(s, k)) 
    print("Output: ", sol.characterReplacementOptimal(s, k)) 
