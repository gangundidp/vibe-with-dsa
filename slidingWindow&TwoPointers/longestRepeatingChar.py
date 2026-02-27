class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency array for A-Z
        freq = [0] * 26

        left = 0
        maxCount = 0
        maxLength = 0

        for right in range(len(s)):

            freq[ord(s[right]) - ord('A')] += 1

            maxCount = max(maxCount, freq[ord(s[right]) - ord('A')])

            while (right - left + 1) - maxCount > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength

if __name__ == "__main__":
    sol = Solution()
    s = "AABABBA"
    k = 1
    # Output: 4
    print("Output: ", sol.characterReplacement(s, k))  
