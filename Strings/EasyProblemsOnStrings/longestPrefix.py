class Solution:
    def longestPrefix(self, s):
        s.sort()
        
        first = s[0]
        last = s[-1]
        ans = ''

        for i in range((min(len(first), len(last)))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break
        
        return ans
    
if __name__ == "__main__":
    sols = Solution()
    s = ['flower', 'flow', 'flight']
    print('Output: ', sols.longestPrefix(s))
            
    s = ['apple', 'banana', 'orange']
    print('Output: ', sols.longestPrefix(s))
            