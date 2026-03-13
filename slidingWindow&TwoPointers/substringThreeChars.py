class Solution:
    def numOfSubstringsBrute(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            freq = {"a": 0, "b": 0, "c": 0}

            for j in range(i, len(s)):
                freq[s[j]] += 1
                
                if freq['a'] > 0 and freq["b"] > 0 and freq["c"] > 0:
                    count += 1
                    
        return count

    def numberOfSubstrings(self, s: str) -> int:
        # Frequency map for 'a', 'b', 'c'
        freq = [0, 0, 0]

        left = 0
        res = 0

        for right in range(len(s)):
            freq[ord(s[right]) - ord('a')] += 1

            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                res += len(s) - right
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    s = "abcabc"
    print("Output: ", sol.numOfSubstringsBrute(s))
    print("Output: ", sol.numberOfSubstrings(s))
